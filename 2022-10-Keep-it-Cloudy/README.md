# Keeping it Cloudy
Downloading from interactive, secure portals while preserving data residency in the cloud.

## We love the cloud
At Bays Consulting, we prefer wherever possible to store and process our clients' data in the cloud,
typically the storage and compute components of Amazon Web Services.

Furthermore, for many of our projects we have contractually agreed requirement that data resides in the cloud at all times,
and is not copied to local employee machines. This generally has two motivations.

Firstly, data protection laws may impose specific geographical data residency requirements, such that personal data
remain within the UK or within the European Economic Area. Such residency requirements are well understood by cloud service providers;
in Amazon's case this in principally covered by the use of specific regions such as `Europe (London)`.

Secondly, the security controls applied to the cloud to monitor and prevent data loss, and to segregate client data, are well understood
and can be documented and audited by our customers.

In addition, keeping the data in the cloud is simply more practical for us, as we can there benefit from Amazon's resilience,
and apply a range of scalable approaches to interrogate and analyse the data; and at the end of the day, for an impatient person like me,
large datasets download too slowly over a home broadband connection!

## So what's the problem?
While the road is generally smooth once data is sitting in our cloud environment (typically Amazon S3), sometimes it's
not obvious how to get it there. 

For publicly available data, one can usually download data straight into a cloud environment by using a utility such as `curl`
from a terminal on a cloud virtual machine. Once on the virtual machine's local storage, another command will take care of
uploading it to S3 or equivalent blob storage.

Often however, a customer will grant us access to download the data from a secure portal, perhaps
a shared folder in Google Drive or Microsoft SharePoint, or some in-house or 3rd-party transfer site. It seems a new method comes
along every day!

Each of these secure web portals will typically have an interactive process for authentication, perhaps involving setting up
an account and often applying Multi-Factor Authentication. So how can we acquire the data directly into the cloud,
without first downloading to a laptop and then re-uploading?

## Avoiding the problem
In this situation, I always aim first to see if there is an alternative to the interactive web portal. 
As well as avoiding the issue of local copy to my laptop, having a direct cloud-to-cloud transfer method ensures
we can transition smoothly to a productionised data pipeline later, even if the current project only involves a single dump of data.

While there is no one-size-fits all approach, some ideas to consider might include:

* Generating some kind of magic link within the secure web portal, if allowed, that can be used directly with `curl`.
* Direct upload by the customer to Amazon S3; we can grant specific authorization to allow data upload to designated drop location,
  either for manual use or as part of a pipeline on the customer side.
* Download from a more headless, machine-friendly portal such as an SFTP site or a Samba mount.
* API or CLI download from the existing portal. 
  Typically, this will require some setup on the customer side to create an API key or equivalent. 
  Check out the following:
  * [CLI for Microsoft 365](https://github.com/pnp/cli-microsoft365)
  * [Google Drive API](https://developers.google.com/drive/api/guides/manage-downloads)

## OK, what else?
If it is not practical to establish one of the methods above, especially if this is a one-off transfer anyway,
we don't have to give up on keeping the data entirely within the cloud. We simply need to launch a web browser that is itself
running within the cloud, and navigate through the interactive download process there.

Since the browser software is running remotely, and all that we are seeing on our laptop is a stream of the pixels
shown on the interactive web portal, the downloaded data itself will never touch even the memory of our local machine.

There are a range of ways to achieve this, from fully managed solutions to more home-grown integrations.

### Amazon Workspaces Web
A recently launched service by Amazon, comprising a fully managed, cloud-hosted browser pixel-streamed to the desktop.

It relies on a SAML-based identity provider for authentication, which could be AWS IAM Identity Center 
(successor to AWS Single Sign-On) if you already have that set up. It can be set up inside a VPC, if you have
requirements to pass internet traffic through a particular NAT or proxy.

There are a few downsides, however.
* It's unclear how the local storage can be accessed, so you would need to re-upload data to S3 via the AWS console inside the browser.
* The pricing is rather off-putting, since you have to pay a certain amount per Monthly Active User, currently $8 in London,
  which makes it very expensive per hour compared to other options.

### Amazon AppStream 2.0
This is a related, but more generic AWS service, designed to stream a variety of applications running in the cloud.
Helpfully, the standard sample image includes Firefox running on a Windows Server backend, perfect for accessing an interactive portal.

As above, the resources can run inside a VPC, allowing access to local VPC endpoints and directing internet traffic
through a particular established route or proxy.

The pricing is much more attractive, being relatively high compared to a base EC2 instance but billed per hour. 
Users can be provisioned in a simple way, without needing to deal in SAML documents!

I gave this a go, creating a Stack and associated Fleet from the Amazon AppStream2 Sample Image.
I made myself a user with entitlements on the stack, immediately receiving an email to my inbox with instructions for 
completing the account set up. Confusingly, an error message popped up to say that I had no applications available,
but after waiting 10-15 minutes for the fleet to initialise fully, and then another couple of minutes to "prepare" my session,
I could open Firefox.

Elastic
Enable default internet access

Graphical performance good enough, a little sluggish
Download itself very fast
Then move manually to Home Folder and it appears in S3 (albeit a specially created bucket)

Harden with copy/paste restrictions

### Windows Server over RDP
Previously my preferred method, one can create a vanilla Windows Server virtual machine using Amazon EC2, billed per hour.

Annoying to install Chrome etc.

### X11 over SSH
If you already have a Linux virtual machine running in the cloud, a venerable option for streaming applications to the desktop
is X11 forwarding over SSH.

Venerable technology. 
Performance better with putty.
* Piggy back on existing SSH


### VNC over SSH
Pros
* Add "AcceptCutText=0", "SendCutText=0"
* Use CLI to re-upload to S3, including use of instance role for AUTHx
* Piggy back on existing SSH


    $env:DISPLAY="127.0.0.1:0.0"

    sudo amazon-linux-extras install firefox
* sudo yum install chromium
* **sudo amazon-linux-extras install epel -y**
* sudo yum install xauth
  echo $DISPLAY
[ec2-user@ip-172-31-9-218 ~]$ echo $DISPLAY
localhost:10.0

https://aws.amazon.com/premiumsupport/knowledge-center/ec2-linux-2-install-gui/

https://aws.amazon.com/appstream2/pricing/


## Conclusion