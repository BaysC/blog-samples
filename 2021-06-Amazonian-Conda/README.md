# The Amazonian Anaconda
(Running an AWS Lambda function against an Anaconda runtime)

## Introduction
As a consulting data scientist, I believe a key strength is flexibility to perform technical work across a range
  of environments, to meet my customer's specific needs.  At the same time, I am always looking for ways to re-use existing work,
  and also to shift data workloads to the cloud wherever possible.

The conda package manager allows the consistent definition of Python runtimes, portable across machines and systems.
In this blog, I shall sketch out how to make the most of this feature, and AWS Lambda can use a conda-defined environment,
  lifting-and-shifting a local workload to the cloud. 


## Why Anaconda?
At Bays Consulting, we are fans of the [Anaconda](https://www.anaconda.com/products/individual-b)
  Python distribution.
Firstly, the packaged desktop software provides a handy entry point for data science,
  bundling tools like Jupyter to get our team up and running fast.
Secondly, on a more technical level, the [conda](https://docs.conda.io/en/latest/) 
  package manager allows us to prepare
  a consistent, predictable specification for a Python runtime with all the right dependencies
  to do our work.  If code runs on one data scientist's machine, we can be confident it will
  run in the same way on another's.

On a further technical note, the packages maintained at [anaconda.org](https://anaconda.org)
  are pre-compiled; getting the right toolchain to compile native code can be a bit painful,
  especially on Windows!

## Mastering the conda
### Creating and updating an environment
Let's first recap how to create a conda environment with some example dependencies, 
and export its definition for re-use.

Assuming we've installed Anaconda, we can create a new, dedicated environment
  for our specific data science work:

    conda create --name blog-test

Let's make that the active environment, and install a couple of dependencies.

    conda activate blog-test
    conda install --channel conda-forge python=3.8 requests pandas

Unpacking the second command a bit:
* We've chosen to take packages from the `conda-forge` channel, which gives us access to the latest and greatest 
  versions of many popular open-source packages.
* We've pinned the core Python version to 3.8, which is a generally available version.
* As an example we've added the additional packages `requests` (for nicer HTTP calls) and `pandas` 
    (for the data science, obviously!).

We can now export the definition of the new environment to a file:

    conda env export --no-build --file blog-test.yml

You can see the results [here](blog-test.yml).  Notice the last line saves the path of the environment on your own machine;
  don't worry about this, as it won't prevent installing the environment in a different place elsewhere.

Note the `--no-build` flag.  This is key if you want your environment to be portable 
  between Windows, Linux and Mac; it saves the packages definitions without specific build numbers,
  which would only be available for one operating system.

### Using that environment
If your colleague takes this file, they can create an identical conda environment of their own by running:

    conda env create --file blog-test.yml

## Cloudy days
### AWS Lambda: deployment package versus image
I promised that the conda environment file would be portable across other machine types.  But what about the cloud?

At Bays Consulting, we are enthusiastic users of Amazon Web Services.  In particular, the AWS Lambda serverless compute
  engine provides a cost-effective way to run smallish tasks, without worrying about creating and maintaining the
  underlying infrastructure.  One supported language runtime is Python, but running a Python script that requires
  dependencies can be tricky.

If you need only a few additional packages, [you can zip them up and supply them to Lambda as a "layer"](https://docs.aws.amazon.com/lambda/latest/dg/python-package-create.html#python-package-create-with-dependency).
AWS imposes a [hard limit](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html), however, of 250 MB
  for the unzipped application runtime, including layers.  This may sound like a lot, but once you start including
  the usual suspects for data science and statistics, you may find yourself breaching this limit.

### Building an image
The solution is to provide a single runtime image with your function code and all dependencies.
I shall now show how to modify Amazon's base Lambda image to use a conda-driven Python runtime environment.
You'll need to install [Docker](https://www.docker.com/products/docker-desktop) to proceed.

The image is defined by a [Dockerfile](Dockerfile), an example of which is available on our GitHub.

If you've not used Docker before, the file may look a bit daunting, so I'll explain line-by-line what's happening.

We use as a base image the existing AWS Lambda runtime for Python 3.8:

    FROM public.ecr.aws/lambda/python:3.8

We make sure the image is up to date, by running the `yum` package manager:

    RUN yum update && yum install -y wget && yum clean all

We download and run the [miniconda](https://docs.conda.io/en/latest/miniconda.html) installer:

    RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o miniconda.sh && sh Miniconda3-latest-Linux-x86_64.sh -b -p /opt/miniconda

We copy our environment file over to the image, strip out any Windows-specific packages, and create a corresponding conda environment:

    COPY blog-test.yml /tmp/environment.yml
    RUN sed -i -r '/m2w64|vs2015|msys2|win|vc/d' /tmp/environment.yml
    RUN /opt/miniconda/bin/conda env create --file /tmp/environment.yml --prefix /opt/conda-env

We install the [AWS Lambda Python Runtime Interface Client](https://pypi.org/project/awslambdaric/); this ensures our image can converse as expected with Lambda. 

    RUN /opt/conda-env/bin/pip install awslambdaric

We now replace the image's existing Python with Python from the conda environment: 

    RUN mv /var/lang/bin/python3.8 /var/lang/bin/python3.8-clean && ln -sf /opt/conda-env/bin/python /var/lang/bin/python3.8

As an example, we copy over a single script to run as our application, which you can see on GitHub [here](example.py): 

    COPY example.py /opt/my-code/example.py

We configure the image's PYTHONPATH to include both dependencies and project code:
    
    ENV PYTHONPATH "/var/lang/lib/python3.8/site-packages:/opt/my-code"

Finally, we configure the image to run the default Lambda entrypoint, and from there call our example function.

    ENTRYPOINT ["/lambda-entrypoint.sh"]
    CMD "example.lambda_handler"

To build and this image, run the following command:

    docker build -t blog-test .

You may find the first run a little slow, but subsequent runs will be quick, since Docker caches unmodified layers.

### Testing the image
I would now go ahead and upload this image to AWS Elastic Container Registry, and then deploy as a Lambda function.
  For now, this is left as an exercise to the reader!
  The AWS documentation [here](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html) is a good starting point.

I'll pick out one tip; how to test the newly built image locally.  Use this command to start a container from the image,
  and map requests to port 9000 to the container's local 8080 port, where the Lambda entrypoint will be listening:

    docker run --rm -it -p 9000:8080 blog-test

Now in a separate window, you can issue requests to this container,
  simulating what Amazon will do when a Lambda function is invoked in the real world:

    curl -d "{}" localhost:9000/2015-03-31/functions/function/invocations

Note that the empty JSON object, `{}`, will be passed as the `event` parameter to our handler function.

Assuming everything has worked, you should see your `curl` returning:

    "Hello World"

And in the container's window, proof that the runtime and dependencies are happy:

    START RequestId: 35839558-0db7-4038-af4e-ba22f63686a7 Version: $LATEST
    Looks like pandas is installed, version 1.2.4
    Looks like requests is installed, version 2.25.1
    END RequestId: 35839558-0db7-4038-af4e-ba22f63686a7


## Conclusion
While the conda environment concept provides a great way to share a set of dependencies between data scientists,
  moving data workloads to the cloud while preserving these dependencies can be daunting.  By supplying AWS Lambda with
  a custom image, we can reuse our existing conda environment definition, and get cracking running our own code in the cloud.

Furthermore, by using a containerised approach, we are not tying ourselves firmly to AWS Lambda, as the same image can be
  executed on a local desktop or server, in AWS Elastic Container Service, or another customer or cloud vendor's container swarm.