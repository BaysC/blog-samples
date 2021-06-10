FROM public.ecr.aws/lambda/python:3.8

RUN yum update && yum install -y wget && yum clean all
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh && sh miniconda.sh -b -p /opt/miniconda
COPY blog-test.yml /tmp/environment.yml
RUN sed -i -r '/m2w64|vs2015|msys2|win|vc/d' /tmp/environment.yml
RUN /opt/miniconda/bin/conda env create --file /tmp/environment.yml --prefix /opt/conda-env
RUN /opt/conda-env/bin/pip install awslambdaric
RUN mv /var/lang/bin/python3.8 /var/lang/bin/python3.8-orig && ln -sf /opt/conda-env/bin/python /var/lang/bin/python3.8
COPY example.py /opt/my-code/example.py

ENV PYTHONPATH "/var/lang/lib/python3.8/site-packages:/opt/my-code"
ENTRYPOINT ["/lambda-entrypoint.sh"]
CMD ["example.lambda_handler"]
