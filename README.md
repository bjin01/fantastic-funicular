# fantastic-funicular

## a small demo sample in python using azure api to grab information and deployed on SUSE Cloud foundry

### *motivation*
*I wanted to write a small app, deploy it on suse cloud foundry and show how easy it is. But I wanted to build an example which can utilize some 3rd party api showing to get data from others out from cloud foundry environment. So I chose Microsoft Azure python SDK to pull some data.*

### *Usage*

On your workstation or laptop or PC clone my repo down to you.

`git clone https://github.com/bjin01/fantastic-funicular.git`

Once you are in the git cloned subdir:

`cf push`

Of course you can adapt the manifest.yml to make it fit to your cloud foundry platform.

The cf push output looks like below:

```Pushing from manifest to org system / space test as admin...
Using manifest file /home/bjin/github/aws-py/manifest.yml
Deprecation warning: Use of 'buildpack' attribute in manifest is deprecated in favor of 'buildpacks'. Please see http://docs.cloudfoundry.org/devguide/deploy-apps/manifest.html#deprecated for alternatives and other app manifest deprecations. This feature will be removed in the future.

Getting app info...
Creating app with these attributes...
+ name:         azureinfo
  path:         /home/bjin/github/aws-py
  buildpacks:
+   python_buildpack
+ command:      python app.py
+ disk quota:   2G
+ memory:       512M
  routes:
+   azureinfo-timely-lynx.bocap.cloud

Creating app azureinfo...
Mapping routes...
Comparing local files to remote cache...
Packaging files to upload...
Uploading files...
 48.55 MiB / 48.55 MiB [==========================================================================================================================================================================================================================================] 100.00% 24s

Waiting for API to complete processing files...

Staging app and tracing logs...
   Downloading python_buildpack...
   Downloaded python_buildpack
   Cell diego-cell-0 creating container for instance d51289de-f6f6-436b-bab1-ab73e066b262
   Cell diego-cell-0 successfully created container for instance d51289de-f6f6-436b-bab1-ab73e066b262
   Downloading app package...
   Downloaded app package (55.1M)
   -----> Python Buildpack version 1.6.27.1
   -----> Supplying Python
   -----> Installing python 2.7.15
          Download [https://cf-buildpacks.suse.com/dependencies/python/python-2.7.15-linux-amd64-sle12-65fbf9f8.tgz]
   -----> Installing setuptools 40.6.3
          Download [https://cf-buildpacks.suse.com/dependencies/setuptools/setuptools-40.6.3-3b474dad.zip]
   -----> Installing pip 9.0.3
          Download [https://cf-buildpacks.suse.com/dependencies/pip/pip-9.0.3-7bf48f9a.tar.gz]
   -----> Installing pip-pop 0.1.1
          Download [https://cf-buildpacks.suse.com/dependencies/pip/pip-pop-0.1.1-f75d0a58.tar.gz]
   -----> Noticed dependency requiring libffi. Bootstrapping libffi.
   -----> Installing libffi 3.2.1
          Download [https://cf-buildpacks.suse.com/dependencies/libffi/libffi-3.2.1-linux-x64-sle12-30384d08.tgz]
   -----> Running Pip Install
          Collecting adal==1.2.1 (from -r /tmp/app/requirements.txt (line 1))
            Downloading https://files.pythonhosted.org/packages/00/72/53dce9e4f5d6c1aa57b8d408cb34dff1969ecbf10ab7e678f32c5e0e2397/adal-1.2.1-py2.py3-none-any.whl (52kB)
          Collecting asn1crypto==0.24.0 (from -r /tmp/app/requirements.txt (line 2))
            Downloading https://files.pythonhosted.org/packages/ea/cd/35485615f45f30a510576f1a56d1e0a7ad7bd8ab5ed7cdc600ef7cd06222/asn1crypto-0.24.0-py2.py3-none-any.whl (101kB)
          
ghts-0.1.0 azure-mgmt-powerbiembedded-2.0.0 azure-mgmt-rdbms-1.9.0 azure-mgmt-recoveryservices-0.3.0 azure-mgmt-recoveryservicesbackup-0.3.0 azure-mgmt-redis-5.0.0 azure-mgmt-relay-0.1.0 azure-mgmt-reservations-0.2.1 azure-mgmt-resource-2.2.0 azure-mgmt-scheduler-2.0.0 azure-mgmt-search-2.1.0 azure-mgmt-servicebus-0.5.3 azure-mgmt-servicefabric-0.2.0 azure-mgmt-signalr-0.1.1 azure-mgmt-sql-0.9.1 azure-mgmt-storage-2.0.0 azure-mgmt-subscription-0.2.0 azure-mgmt-trafficmanager-0.50.0 azure-mgmt-web-0.35.0 azure-nspkg-3.0.2 certifi-2019.6.16 cffi-1.12.3 chardet-3.0.4 cryptography-2.7 enum34-1.1.6 futures-3.2.0 idna-2.8 ipaddress-1.0.22 isodate-0.6.0 itsdangerous-1.1.0 msrest-0.6.8 msrestazure-0.6.1 oauthlib-3.0.1 pathlib2-2.3.4 pycparser-2.19 python-dateutil-2.8.0 requests-2.22.0 requests-oauthlib-1.2.0 scandir-1.10.0 six-1.12.0 typing-3.7.4 urllib3-1.25.3
          You are using pip version 9.0.3, however version 19.1.1 is available.
          You should consider upgrading via the 'pip install --upgrade pip' command.
   Exit status 0
   Uploading droplet, build artifacts cache...
   Uploading droplet...
   Uploading build artifacts cache...
   Uploaded build artifacts cache (57.8M)
   Uploaded droplet (81.5M)
   Uploading complete
   Cell diego-cell-0 stopping instance d51289de-f6f6-436b-bab1-ab73e066b262
   Cell diego-cell-0 destroying container for instance d51289de-f6f6-436b-bab1-ab73e066b262
   Cell diego-cell-0 successfully destroyed container for instance d51289de-f6f6-436b-bab1-ab73e066b262

Waiting for app to start...

name:              azureinfo
requested state:   started
routes:            azureinfo-timely-lynx.bocap.cloud
last uploaded:     Tue 09 Jul 17:57:47 CEST 2019
stack:             sle12
buildpacks:        python

type:            web
instances:       1/1
memory usage:    512M
start command:   python app.py
     state     since                  cpu    memory         disk         details
#0   running   2019-07-09T15:58:44Z   0.0%   1.8M of 512M   224K of 2G


`


