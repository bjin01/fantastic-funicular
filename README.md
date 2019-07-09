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
`Pushing from manifest to org system / space test as admin...
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
          Collecting azure-common==1.1.23 (from -r /tmp/app/requirements.txt (line 3))
            Downloading https://files.pythonhosted.org/packages/00/55/a703923c12cd3172d5c007beda0c1a34342a17a6a72779f8a7c269af0cd6/azure_common-1.1.23-py2.py3-none-any.whl
          Collecting azure-mgmt==4.0.0 (from -r /tmp/app/requirements.txt (line 4))
            Downloading https://files.pythonhosted.org/packages/19/8e/6fa401c437579127e726487582a9861fef09022c4ab50901bb499a8e4fc1/azure_mgmt-4.0.0-py2.py3-none-any.whl
          Collecting azure-mgmt-advisor==1.0.1 (from -r /tmp/app/requirements.txt (line 5))
            Downloading https://files.pythonhosted.org/packages/cb/f3/a86ba3e0784d12c8fe5cbf1f24e1b9255575a2f0892e08c46cddd0795dfd/azure_mgmt_advisor-1.0.1-py2.py3-none-any.whl
          Collecting azure-mgmt-applicationinsights==0.1.1 (from -r /tmp/app/requirements.txt (line 6))
            Downloading https://files.pythonhosted.org/packages/30/61/1d95a5ef3a9119a0d375d8670129375515de20e20409612e9671c99bd19f/azure_mgmt_applicationinsights-0.1.1-py2.py3-none-any.whl (42kB)
          Collecting azure-mgmt-authorization==0.50.0 (from -r /tmp/app/requirements.txt (line 7))
            Downloading https://files.pythonhosted.org/packages/6f/17/55b974603c16be89c7a7c16bac57b7bce48527bf1bebc3f116f7215176e6/azure_mgmt_authorization-0.50.0-py2.py3-none-any.whl (81kB)
          Collecting azure-mgmt-batch==5.0.1 (from -r /tmp/app/requirements.txt (line 8))
            Downloading https://files.pythonhosted.org/packages/97/81/a9eb3fd2ab070159105b4cfe9640c24410ac8195286729d62bfdf871de94/azure_mgmt_batch-5.0.1-py2.py3-none-any.whl (87kB)
          Collecting azure-mgmt-batchai==2.0.0 (from -r /tmp/app/requirements.txt (line 9))
            Downloading https://files.pythonhosted.org/packages/d9/a5/ab796c2a490155c14f9ac4240724ca5c56723315d4dc753030712e6f2e80/azure_mgmt_batchai-2.0.0-py2.py3-none-any.whl (174kB)
          Collecting azure-mgmt-billing==0.2.0 (from -r /tmp/app/requirements.txt (line 10))
            Downloading https://files.pythonhosted.org/packages/0f/24/5106287ea0f6562d965afb055e3c6c0da058f7844a70464e67bab56c6c4b/azure_mgmt_billing-0.2.0-py2.py3-none-any.whl
          Collecting azure-mgmt-cdn==3.1.0 (from -r /tmp/app/requirements.txt (line 11))
            Downloading https://files.pythonhosted.org/packages/97/bf/c41e8985b4ffaaad2baaded1fb7b113433ae2d30d65c1a8c226e72284b72/azure_mgmt_cdn-3.1.0-py2.py3-none-any.whl (119kB)
          Collecting azure-mgmt-cognitiveservices==3.0.0 (from -r /tmp/app/requirements.txt (line 12))
            Downloading https://files.pythonhosted.org/packages/8d/c8/222ea2f533c6b8f8656f3091101b4c3aa32c162d2a609d07d1ae00172515/azure_mgmt_cognitiveservices-3.0.0-py2.py3-none-any.whl (58kB)
          Collecting azure-mgmt-commerce==1.0.1 (from -r /tmp/app/requirements.txt (line 13))
            Downloading https://files.pythonhosted.org/packages/7e/13/f421e77dd1fe3c9657a890f9c085f433fe422f54003ee03e631a8be5c4e7/azure_mgmt_commerce-1.0.1-py2.py3-none-any.whl
          Collecting azure-mgmt-compute==4.6.2 (from -r /tmp/app/requirements.txt (line 14))
            Downloading https://files.pythonhosted.org/packages/0e/4d/7ac30585c567a8b9fe8294e0e956c6ef48665522ddf8f8c44bf38b700798/azure_mgmt_compute-4.6.2-py2.py3-none-any.whl (3.0MB)
          Collecting azure-mgmt-consumption==2.0.0 (from -r /tmp/app/requirements.txt (line 15))
            Downloading https://files.pythonhosted.org/packages/11/f4/2db9557494dfb17ff3edeae5726981143a7baace17df3712b189e343bd8c/azure_mgmt_consumption-2.0.0-py2.py3-none-any.whl (46kB)
          Collecting azure-mgmt-containerinstance==1.5.0 (from -r /tmp/app/requirements.txt (line 16))
            Downloading https://files.pythonhosted.org/packages/fd/d1/d770050f20ad81b80f7eb41f89e1a5d841cf74bf41c7e1ff137c46f28a1e/azure_mgmt_containerinstance-1.5.0-py2.py3-none-any.whl (96kB)
          Collecting azure-mgmt-containerregistry==2.8.0 (from -r /tmp/app/requirements.txt (line 17))
            Downloading https://files.pythonhosted.org/packages/97/70/8c2d0509db466678eba16fa2b0a539499f3b351b1f2993126ad843d5be13/azure_mgmt_containerregistry-2.8.0-py2.py3-none-any.whl (718kB)
          Collecting azure-mgmt-containerservice==4.4.0 (from -r /tmp/app/requirements.txt (line 18))
            Downloading https://files.pythonhosted.org/packages/5b/2f/0eba2dbd5d3f66c076a66b0020ccfe9c7e78534ac132afaa104c138680c1/azure_mgmt_containerservice-4.4.0-py2.py3-none-any.whl (206kB)
          Collecting azure-mgmt-cosmosdb==0.4.1 (from -r /tmp/app/requirements.txt (line 19))
            Downloading https://files.pythonhosted.org/packages/17/ed/d97a04c8c26e2432f2cf000b711daeb053e1cfbdb046bd5d070c941b4fcb/azure_mgmt_cosmosdb-0.4.1-py2.py3-none-any.whl (100kB)
          Collecting azure-mgmt-datafactory==0.6.0 (from -r /tmp/app/requirements.txt (line 20))
            Downloading https://files.pythonhosted.org/packages/cf/01/32a6ad5ad348d965f7c106d819a1f6dc613f6aa98a720ffc529ef468016b/azure_mgmt_datafactory-0.6.0-py2.py3-none-any.whl (418kB)
          Collecting azure-mgmt-datalake-analytics==0.6.0 (from -r /tmp/app/requirements.txt (line 21))
            Downloading https://files.pythonhosted.org/packages/73/e7/5d909ef5812fc31f2871f3510ef43af93157ba51be03b6f798afba7a29d8/azure_mgmt_datalake_analytics-0.6.0-py2.py3-none-any.whl (288kB)
          Collecting azure-mgmt-datalake-nspkg==3.0.1 (from -r /tmp/app/requirements.txt (line 22))
            Downloading https://files.pythonhosted.org/packages/76/e2/4271ab409ff3bac77ae2843c30590868db42715a75658f8a9da229b7ac98/azure_mgmt_datalake_nspkg-3.0.1-py2-none-any.whl
          Collecting azure-mgmt-datalake-store==0.5.0 (from -r /tmp/app/requirements.txt (line 23))
            Downloading https://files.pythonhosted.org/packages/ff/ac/5685cd06dc8b245bb6b894815764a14bd62245ba4579b45148682f510fdd/azure_mgmt_datalake_store-0.5.0-py2.py3-none-any.whl (88kB)
          Collecting azure-mgmt-datamigration==1.0.0 (from -r /tmp/app/requirements.txt (line 24))
            Downloading https://files.pythonhosted.org/packages/8b/4f/7b149487e77d94e701288e1d0b066a7d522bdfe8595e992b5d39dfb00f80/azure_mgmt_datamigration-1.0.0-py2.py3-none-any.whl (185kB)
          Collecting azure-mgmt-devspaces==0.1.0 (from -r /tmp/app/requirements.txt (line 25))
            Downloading https://files.pythonhosted.org/packages/f4/d3/ff9c39578f24fb4bd158a882788c7795b177cf3f23ce7cf1d8b52066a64e/azure_mgmt_devspaces-0.1.0-py2.py3-none-any.whl
          Collecting azure-mgmt-devtestlabs==2.2.0 (from -r /tmp/app/requirements.txt (line 26))
            Downloading https://files.pythonhosted.org/packages/2f/93/a64abaede2fc6a52476af8ceab9cedb368c49e948d9385cbe7cd4ce5ffff/azure_mgmt_devtestlabs-2.2.0-py2.py3-none-any.whl (194kB)
          Collecting azure-mgmt-dns==2.1.0 (from -r /tmp/app/requirements.txt (line 27))
            Downloading https://files.pythonhosted.org/packages/c7/d7/0f986a64b06db93cf29b76f9a188f5778eb959624a00ed6aedc335ee58d2/azure_mgmt_dns-2.1.0-py2.py3-none-any.whl (134kB)
          Collecting azure-mgmt-eventgrid==1.0.0 (from -r /tmp/app/requirements.txt (line 28))
            Downloading https://files.pythonhosted.org/packages/54/5b/e91e616021ae9be0019c9c19cffb92b97d787246ca51cfcc0b0a0c6da77a/azure_mgmt_eventgrid-1.0.0-py2.py3-none-any.whl (51kB)
          Collecting azure-mgmt-eventhub==2.6.0 (from -r /tmp/app/requirements.txt (line 29))
            Downloading https://files.pythonhosted.org/packages/5a/cb/3822bcfa815f894c86a27845ae4160c0169722598399234cd6f77bb82347/azure_mgmt_eventhub-2.6.0-py2.py3-none-any.whl (189kB)
          Collecting azure-mgmt-hanaonazure==0.1.1 (from -r /tmp/app/requirements.txt (line 30))
            Downloading https://files.pythonhosted.org/packages/f3/1b/50d300ae02158ab092f923132050b56c148f1b784c7b594d3275d4449769/azure_mgmt_hanaonazure-0.1.1-py2.py3-none-any.whl
          Collecting azure-mgmt-iotcentral==0.1.0 (from -r /tmp/app/requirements.txt (line 31))
            Downloading https://files.pythonhosted.org/packages/58/4e/e2e5f2d545a46ada3705c85c45c12882a443d40f60e1a908c78058e15cf2/azure_mgmt_iotcentral-0.1.0-py2.py3-none-any.whl
          Collecting azure-mgmt-iothub==0.5.0 (from -r /tmp/app/requirements.txt (line 32))
            Downloading https://files.pythonhosted.org/packages/19/d6/b422df467b3d7f4e2975b590fbf6e12aaae0a497c7d080b4955a6a6d794a/azure_mgmt_iothub-0.5.0-py2.py3-none-any.whl (102kB)
          Collecting azure-mgmt-iothubprovisioningservices==0.2.0 (from -r /tmp/app/requirements.txt (line 33))
            Downloading https://files.pythonhosted.org/packages/84/ce/3500c731a5c5b31028e662aa41bc45f75301834a0c03adeacfe7ef7bd86e/azure_mgmt_iothubprovisioningservices-0.2.0-py2.py3-none-any.whl (60kB)
          Collecting azure-mgmt-keyvault==1.1.0 (from -r /tmp/app/requirements.txt (line 34))
            Downloading https://files.pythonhosted.org/packages/49/de/0d69aedae7c5f6428314640b65947203ab80409c12b5d4e66fb5b7a4182e/azure_mgmt_keyvault-1.1.0-py2.py3-none-any.whl (111kB)
          Collecting azure-mgmt-loganalytics==0.2.0 (from -r /tmp/app/requirements.txt (line 35))
            Downloading https://files.pythonhosted.org/packages/70/40/c9b77bf82916e963aa701fb396673f7ddc4cdab95524b6d2edf927b05630/azure_mgmt_loganalytics-0.2.0-py2.py3-none-any.whl (89kB)
          Collecting azure-mgmt-logic==3.0.0 (from -r /tmp/app/requirements.txt (line 36))
            Downloading https://files.pythonhosted.org/packages/88/98/693c515e97043520f5cebf1ecae7bf198df100f5f9870b53d4be3bcaa5ce/azure_mgmt_logic-3.0.0-py2.py3-none-any.whl (303kB)
          Collecting azure-mgmt-machinelearningcompute==0.4.1 (from -r /tmp/app/requirements.txt (line 37))
            Downloading https://files.pythonhosted.org/packages/b4/9c/f8eb81b307df4465809b182f2fe44c288eeb41c0ab54f91b61ac554998a9/azure_mgmt_machinelearningcompute-0.4.1-py2.py3-none-any.whl
          Collecting azure-mgmt-managementgroups==0.1.0 (from -r /tmp/app/requirements.txt (line 38))
            Downloading https://files.pythonhosted.org/packages/f2/50/591adac2a6cd8d77cccd38bdf5d177ad6a2e95b9217daa9a60b5d86de5cd/azure_mgmt_managementgroups-0.1.0-py2.py3-none-any.whl (59kB)
          Collecting azure-mgmt-managementpartner==0.1.1 (from -r /tmp/app/requirements.txt (line 39))
            Downloading https://files.pythonhosted.org/packages/9a/91/2bccd2bdca4158a7b6169538b25e22e0b4f8ff835754888aab45ffbd0448/azure_mgmt_managementpartner-0.1.1-py2.py3-none-any.whl
          Collecting azure-mgmt-maps==0.1.0 (from -r /tmp/app/requirements.txt (line 40))
            Downloading https://files.pythonhosted.org/packages/e4/04/c64326729e842f3eab1fd527f7582e269e4b0e5b9324a4562edaf0371953/azure_mgmt_maps-0.1.0-py2.py3-none-any.whl
          Collecting azure-mgmt-marketplaceordering==0.1.0 (from -r /tmp/app/requirements.txt (line 41))
            Downloading https://files.pythonhosted.org/packages/a8/cb/13502fdbaf520d08fb280eb31ecfe5d926b9cf92259c22280bbde96b307d/azure_mgmt_marketplaceordering-0.1.0-py2.py3-none-any.whl
          Collecting azure-mgmt-media==1.0.0 (from -r /tmp/app/requirements.txt (line 42))
            Downloading https://files.pythonhosted.org/packages/65/2e/6d9649bd5645ac32a179adfea5707f640fc51a57e493c27f0ab575789e85/azure_mgmt_media-1.0.0-py2.py3-none-any.whl (335kB)
          Collecting azure-mgmt-monitor==0.5.2 (from -r /tmp/app/requirements.txt (line 43))
            Downloading https://files.pythonhosted.org/packages/6a/3b/a8b95ee25f1c209ad82ad06de39f4efbfb9dc8a8dc5da5a7a48d7897bf3e/azure_mgmt_monitor-0.5.2-py2.py3-none-any.whl (247kB)
          Collecting azure-mgmt-msi==0.2.0 (from -r /tmp/app/requirements.txt (line 44))
            Downloading https://files.pythonhosted.org/packages/ae/95/b451721e38ca0feddce03ee3ce86158e208d0150253bd371207a8df4e9c5/azure_mgmt_msi-0.2.0-py2.py3-none-any.whl
          Collecting azure-mgmt-network==2.7.0 (from -r /tmp/app/requirements.txt (line 45))
            Downloading https://files.pythonhosted.org/packages/61/95/d63833e95406626256893a2f3ef4e5029a168330e3a27817a9f5597c0e6f/azure_mgmt_network-2.7.0-py2.py3-none-any.whl (11.4MB)
          Collecting azure-mgmt-notificationhubs==2.1.0 (from -r /tmp/app/requirements.txt (line 46))
            Downloading https://files.pythonhosted.org/packages/55/c0/62a0495583dfc44830f711be52cb4a4e116c2f72c89a19b90d654bdafc4a/azure_mgmt_notificationhubs-2.1.0-py2.py3-none-any.whl (76kB)
          Collecting azure-mgmt-nspkg==3.0.2 (from -r /tmp/app/requirements.txt (line 47))
            Downloading https://files.pythonhosted.org/packages/a1/6e/464d039ec6184234b188d6a9d199e658cce86b38afe4db0e8edd1629f3f6/azure_mgmt_nspkg-3.0.2-py2-none-any.whl
          Collecting azure-mgmt-policyinsights==0.1.0 (from -r /tmp/app/requirements.txt (line 48))
            Downloading https://files.pythonhosted.org/packages/19/84/7021951ae69572a19af0ff9cca1d2abf3542d35af38796656ded1be08358/azure_mgmt_policyinsights-0.1.0-py2.py3-none-any.whl (44kB)
          Collecting azure-mgmt-powerbiembedded==2.0.0 (from -r /tmp/app/requirements.txt (line 49))
            Downloading https://files.pythonhosted.org/packages/64/2b/5a69d118626a83055ce577fb6ba35c114e72f0273d0c4d943b909ee8d51e/azure_mgmt_powerbiembedded-2.0.0-py2.py3-none-any.whl
          Collecting azure-mgmt-rdbms==1.9.0 (from -r /tmp/app/requirements.txt (line 50))
            Downloading https://files.pythonhosted.org/packages/d2/94/c850c8257d19b08eb6b03154d6fe21938801562b4082d27985f54ebe9de4/azure_mgmt_rdbms-1.9.0-py2.py3-none-any.whl (259kB)
          Collecting azure-mgmt-recoveryservices==0.3.0 (from -r /tmp/app/requirements.txt (line 51))
            Downloading https://files.pythonhosted.org/packages/fd/7f/80327a27e03473101afb136e872279ad1386adf1bac14a58a9f839cd8352/azure_mgmt_recoveryservices-0.3.0-py2.py3-none-any.whl (70kB)
          Collecting azure-mgmt-recoveryservicesbackup==0.3.0 (from -r /tmp/app/requirements.txt (line 52))
            Downloading https://files.pythonhosted.org/packages/c5/af/13b10d76bc0ff9188c9e5cd9f2726a5745029b76125938491f9abac5399d/azure_mgmt_recoveryservicesbackup-0.3.0-py2.py3-none-any.whl (568kB)
          Collecting azure-mgmt-redis==5.0.0 (from -r /tmp/app/requirements.txt (line 53))
            Downloading https://files.pythonhosted.org/packages/90/a7/42342a984b2916972c5c5e24df94e3cd5e4377a8dc465a83415706d9be6f/azure_mgmt_redis-5.0.0-py2.py3-none-any.whl (43kB)
          Collecting azure-mgmt-relay==0.1.0 (from -r /tmp/app/requirements.txt (line 54))
            Downloading https://files.pythonhosted.org/packages/00/f7/f5c72bd19829cfaf9f070ec294c901ad7f98835ba9560fdad652afb1071f/azure_mgmt_relay-0.1.0-py2.py3-none-any.whl
          Collecting azure-mgmt-reservations==0.2.1 (from -r /tmp/app/requirements.txt (line 55))
            Downloading https://files.pythonhosted.org/packages/a9/2b/e0edb8dbe85e447005cde508b869e564f58270f631219f036d8ab71184f9/azure_mgmt_reservations-0.2.1-py2.py3-none-any.whl (50kB)
          Collecting azure-mgmt-resource==2.2.0 (from -r /tmp/app/requirements.txt (line 56))
            Downloading https://files.pythonhosted.org/packages/1b/2d/9c3f2c9bf6e19f3efe4ddcaa946ea515d5229f4c0b387e224267e77fb73b/azure_mgmt_resource-2.2.0-py2.py3-none-any.whl (780kB)
          Collecting azure-mgmt-scheduler==2.0.0 (from -r /tmp/app/requirements.txt (line 57))
            Downloading https://files.pythonhosted.org/packages/e8/55/f3490698ff622244438e667e0321808e84389e69c5fb77a1d6db869d9bb7/azure_mgmt_scheduler-2.0.0-py2.py3-none-any.whl (67kB)
          Collecting azure-mgmt-search==2.1.0 (from -r /tmp/app/requirements.txt (line 58))
            Downloading https://files.pythonhosted.org/packages/c9/18/fa4e0d541332c0ba6ef16beaa9b55f831436949e7d0981d5677dff2ddfb5/azure_mgmt_search-2.1.0-py2.py3-none-any.whl (41kB)
          Collecting azure-mgmt-servicebus==0.5.3 (from -r /tmp/app/requirements.txt (line 59))
            Downloading https://files.pythonhosted.org/packages/28/ad/9e90f8bab40a9682410e57ed08a799be113c5e470bec247b099038c6389e/azure_mgmt_servicebus-0.5.3-py2.py3-none-any.whl (112kB)
          Collecting azure-mgmt-servicefabric==0.2.0 (from -r /tmp/app/requirements.txt (line 60))
            Downloading https://files.pythonhosted.org/packages/6e/06/fafe8b5d881cfa68927e61557c8419dcfacb93e07f4ab17cc60959707a53/azure_mgmt_servicefabric-0.2.0-py2.py3-none-any.whl (142kB)
          Collecting azure-mgmt-signalr==0.1.1 (from -r /tmp/app/requirements.txt (line 61))
            Downloading https://files.pythonhosted.org/packages/10/32/379137548a4c6e4dfd15da6b1c476f2b1af52e8d7fe243fdac9ea2064427/azure_mgmt_signalr-0.1.1-py2.py3-none-any.whl (49kB)
          Collecting azure-mgmt-sql==0.9.1 (from -r /tmp/app/requirements.txt (line 62))
            Downloading https://files.pythonhosted.org/packages/c5/bb/219c76af961e9e6d1f5055d70c3cc06889b91375727a04367149c3aad640/azure_mgmt_sql-0.9.1-py2.py3-none-any.whl (485kB)
          Collecting azure-mgmt-storage==2.0.0 (from -r /tmp/app/requirements.txt (line 63))
            Downloading https://files.pythonhosted.org/packages/67/5b/15e6a8109af53e4c2228142ea816532036700757d035fc1b9cd0f6a63b02/azure_mgmt_storage-2.0.0-py2.py3-none-any.whl (558kB)
          Collecting azure-mgmt-subscription==0.2.0 (from -r /tmp/app/requirements.txt (line 64))
            Downloading https://files.pythonhosted.org/packages/27/72/f63f72d9c27659f96aae287f7ba67c9ba2877213c2c10d8b797e0dee5059/azure_mgmt_subscription-0.2.0-py2.py3-none-any.whl (40kB)
          Collecting azure-mgmt-trafficmanager==0.50.0 (from -r /tmp/app/requirements.txt (line 65))
            Downloading https://files.pythonhosted.org/packages/ed/4f/c322d72dc92dde543471bc23f9ac0eb6b9d0dc2441bb5ce938250040e307/azure_mgmt_trafficmanager-0.50.0-py2.py3-none-any.whl (52kB)
          Collecting azure-mgmt-web==0.35.0 (from -r /tmp/app/requirements.txt (line 66))
            Downloading https://files.pythonhosted.org/packages/21/04/3f2622720664c972d927fd9e58c0066e998739b7891649207765be674126/azure_mgmt_web-0.35.0-py2.py3-none-any.whl (358kB)
          Collecting azure-nspkg==3.0.2 (from -r /tmp/app/requirements.txt (line 67))
            Downloading https://files.pythonhosted.org/packages/c2/95/af354f2f415d250dafe26a5d94230558aa8cf733a9dcbf0d26cd61f5a9b8/azure_nspkg-3.0.2-py2-none-any.whl
          Collecting certifi==2019.6.16 (from -r /tmp/app/requirements.txt (line 68))
            Downloading https://files.pythonhosted.org/packages/69/1b/b853c7a9d4f6a6d00749e94eb6f3a041e342a885b87340b79c1ef73e3a78/certifi-2019.6.16-py2.py3-none-any.whl (157kB)
          Collecting cffi==1.12.3 (from -r /tmp/app/requirements.txt (line 69))
            Downloading https://files.pythonhosted.org/packages/8d/e9/0c8afd1579e5cf7bc0f06fbcd7cdb954cbc0baadd505973949a99337da1c/cffi-1.12.3-cp27-cp27mu-manylinux1_x86_64.whl (415kB)
          Collecting chardet==3.0.4 (from -r /tmp/app/requirements.txt (line 70))
            Downloading https://files.pythonhosted.org/packages/bc/a9/01ffebfb562e4274b6487b4bb1ddec7ca55ec7510b22e4c51f14098443b8/chardet-3.0.4-py2.py3-none-any.whl (133kB)
          Collecting Click==7.0 (from -r /tmp/app/requirements.txt (line 71))
            Downloading https://files.pythonhosted.org/packages/fa/37/45185cb5abbc30d7257104c434fe0b07e5a195a6847506c074527aa599ec/Click-7.0-py2.py3-none-any.whl (81kB)
          Collecting cryptography==2.7 (from -r /tmp/app/requirements.txt (line 72))
            Downloading https://files.pythonhosted.org/packages/e6/68/50698ce24c61db7d44d93a5043c621a0ca7839d4ef9dff913e6ab465fc92/cryptography-2.7-cp27-cp27mu-manylinux1_x86_64.whl (2.3MB)
          Collecting enum34==1.1.6 (from -r /tmp/app/requirements.txt (line 73))
            Downloading https://files.pythonhosted.org/packages/c5/db/e56e6b4bbac7c4a06de1c50de6fe1ef3810018ae11732a50f15f62c7d050/enum34-1.1.6-py2-none-any.whl
          Collecting Flask==1.0.3 (from -r /tmp/app/requirements.txt (line 74))
            Downloading https://files.pythonhosted.org/packages/9a/74/670ae9737d14114753b8c8fdf2e8bd212a05d3b361ab15b44937dfd40985/Flask-1.0.3-py2.py3-none-any.whl (92kB)
          Collecting Flask-WTF==0.14.2 (from -r /tmp/app/requirements.txt (line 75))
            Downloading https://files.pythonhosted.org/packages/60/3a/58c629472d10539ae5167dc7c1fecfa95dd7d0b7864623931e3776438a24/Flask_WTF-0.14.2-py2.py3-none-any.whl
          Collecting futures==3.2.0 (from -r /tmp/app/requirements.txt (line 76))
            Downloading https://files.pythonhosted.org/packages/2d/99/b2c4e9d5a30f6471e410a146232b4118e697fa3ffc06d6a65efde84debd0/futures-3.2.0-py2-none-any.whl
          Collecting idna==2.8 (from -r /tmp/app/requirements.txt (line 77))
            Downloading https://files.pythonhosted.org/packages/14/2c/cd551d81dbe15200be1cf41cd03869a46fe7226e7450af7a6545bfc474c9/idna-2.8-py2.py3-none-any.whl (58kB)
          Collecting ipaddress==1.0.22 (from -r /tmp/app/requirements.txt (line 78))
            Downloading https://files.pythonhosted.org/packages/fc/d0/7fc3a811e011d4b388be48a0e381db8d990042df54aa4ef4599a31d39853/ipaddress-1.0.22-py2.py3-none-any.whl
          Collecting isodate==0.6.0 (from -r /tmp/app/requirements.txt (line 79))
            Downloading https://files.pythonhosted.org/packages/9b/9f/b36f7774ff5ea8e428fdcfc4bb332c39ee5b9362ddd3d40d9516a55221b2/isodate-0.6.0-py2.py3-none-any.whl (45kB)
          Collecting itsdangerous==1.1.0 (from -r /tmp/app/requirements.txt (line 80))
            Downloading https://files.pythonhosted.org/packages/76/ae/44b03b253d6fade317f32c24d100b3b35c2239807046a4c953c7b89fa49e/itsdangerous-1.1.0-py2.py3-none-any.whl
          Collecting Jinja2==2.10.1 (from -r /tmp/app/requirements.txt (line 81))
            Downloading https://files.pythonhosted.org/packages/1d/e7/fd8b501e7a6dfe492a433deb7b9d833d39ca74916fa8bc63dd1a4947a671/Jinja2-2.10.1-py2.py3-none-any.whl (124kB)
          Collecting MarkupSafe==1.1.1 (from -r /tmp/app/requirements.txt (line 82))
            Downloading https://files.pythonhosted.org/packages/fb/40/f3adb7cf24a8012813c5edb20329eb22d5d8e2a0ecf73d21d6b85865da11/MarkupSafe-1.1.1-cp27-cp27mu-manylinux1_x86_64.whl
          Collecting msrest==0.6.8 (from -r /tmp/app/requirements.txt (line 83))
            Downloading https://files.pythonhosted.org/packages/56/1d/a5947aba03169aeccd2d6539a3986614d133be53adac028ec3d6a1a285a4/msrest-0.6.8-py2.py3-none-any.whl (82kB)
          Collecting msrestazure==0.6.1 (from -r /tmp/app/requirements.txt (line 84))
            Downloading https://files.pythonhosted.org/packages/0a/aa/b17a4f702ecd6d9e989ae34109aa384c988aed0de37215c651165ed45238/msrestazure-0.6.1-py2.py3-none-any.whl (40kB)
          Collecting oauthlib==3.0.1 (from -r /tmp/app/requirements.txt (line 85))
            Downloading https://files.pythonhosted.org/packages/16/95/699466b05b72b94a41f662dc9edf87fda4289e3602ecd42d27fcaddf7b56/oauthlib-3.0.1-py2.py3-none-any.whl (142kB)
          Collecting pathlib2==2.3.4 (from -r /tmp/app/requirements.txt (line 86))
            Downloading https://files.pythonhosted.org/packages/67/c6/4dbf5dfdbe1140cadf765c3896acc098578626c35721bc7d3eb35f6a8fc1/pathlib2-2.3.4-py2.py3-none-any.whl
          Collecting pycparser==2.19 (from -r /tmp/app/requirements.txt (line 87))
            Downloading https://files.pythonhosted.org/packages/68/9e/49196946aee219aead1290e00d1e7fdeab8567783e83e1b9ab5585e6206a/pycparser-2.19.tar.gz (158kB)
          Collecting PyJWT==1.7.1 (from -r /tmp/app/requirements.txt (line 88))
            Downloading https://files.pythonhosted.org/packages/87/8b/6a9f14b5f781697e51259d81657e6048fd31a113229cf346880bb7545565/PyJWT-1.7.1-py2.py3-none-any.whl
          Collecting python-dateutil==2.8.0 (from -r /tmp/app/requirements.txt (line 89))
            Downloading https://files.pythonhosted.org/packages/41/17/c62faccbfbd163c7f57f3844689e3a78bae1f403648a6afb1d0866d87fbb/python_dateutil-2.8.0-py2.py3-none-any.whl (226kB)
          Collecting requests==2.22.0 (from -r /tmp/app/requirements.txt (line 90))
            Downloading https://files.pythonhosted.org/packages/51/bd/23c926cd341ea6b7dd0b2a00aba99ae0f828be89d72b2190f27c11d4b7fb/requests-2.22.0-py2.py3-none-any.whl (57kB)
          Collecting requests-oauthlib==1.2.0 (from -r /tmp/app/requirements.txt (line 91))
            Downloading https://files.pythonhosted.org/packages/c2/e2/9fd03d55ffb70fe51f587f20bcf407a6927eb121de86928b34d162f0b1ac/requests_oauthlib-1.2.0-py2.py3-none-any.whl
          Collecting scandir==1.10.0 (from -r /tmp/app/requirements.txt (line 92))
            Downloading https://files.pythonhosted.org/packages/df/f5/9c052db7bd54d0cbf1bc0bb6554362bba1012d03e5888950a4f5c5dadc4e/scandir-1.10.0.tar.gz
          Collecting six==1.12.0 (from -r /tmp/app/requirements.txt (line 93))
            Downloading https://files.pythonhosted.org/packages/73/fb/00a976f728d0d1fecfe898238ce23f502a721c0ac0ecfedb80e0d88c64e9/six-1.12.0-py2.py3-none-any.whl
          Collecting typing==3.7.4 (from -r /tmp/app/requirements.txt (line 94))
            Downloading https://files.pythonhosted.org/packages/79/be/e43ccd1317f483e14de507787322c74092a688707d02fa5f16562270eb63/typing-3.7.4-py2-none-any.whl
          Collecting urllib3==1.25.3 (from -r /tmp/app/requirements.txt (line 95))
            Downloading https://files.pythonhosted.org/packages/e6/60/247f23a7121ae632d62811ba7f273d0e58972d75e58a94d329d51550a47d/urllib3-1.25.3-py2.py3-none-any.whl (150kB)
          Collecting Werkzeug==0.15.4 (from -r /tmp/app/requirements.txt (line 96))
            Downloading https://files.pythonhosted.org/packages/9f/57/92a497e38161ce40606c27a86759c6b92dd34fcdb33f64171ec559257c02/Werkzeug-0.15.4-py2.py3-none-any.whl (327kB)
          Collecting WTForms==2.2.1 (from -r /tmp/app/requirements.txt (line 97))
            Downloading https://files.pythonhosted.org/packages/9f/c8/dac5dce9908df1d9d48ec0e26e2a250839fa36ea2c602cc4f85ccfeb5c65/WTForms-2.2.1-py2.py3-none-any.whl (166kB)
          Installing collected packages: asn1crypto, enum34, ipaddress, pycparser, cffi, six, cryptography, python-dateutil, urllib3, certifi, chardet, idna, requests, PyJWT, adal, azure-nspkg, azure-common, isodate, oauthlib, requests-oauthlib, typing, msrest, msrestazure, azure-mgmt-nspkg, azure-mgmt-iothub, azure-mgmt-notificationhubs, azure-mgmt-resource, azure-mgmt-servicefabric, azure-mgmt-redis, azure-mgmt-keyvault, azure-mgmt-eventhub, azure-mgmt-dns, azure-mgmt-msi, azure-mgmt-storage, azure-mgmt-media, azure-mgmt-consumption, azure-mgmt-applicationinsights, azure-mgmt-recoveryservicesbackup, azure-mgmt-signalr, azure-mgmt-hanaonazure, azure-mgmt-logic, azure-mgmt-trafficmanager, azure-mgmt-containerservice, azure-mgmt-cognitiveservices, azure-mgmt-reservations, azure-mgmt-recoveryservices, azure-mgmt-web, azure-mgmt-subscription, azure-mgmt-search, azure-mgmt-commerce, azure-mgmt-marketplaceordering, azure-mgmt-billing, azure-mgmt-policyinsights, azure-mgmt-datamigration, azure-mgmt-machinelearningcompute, azure-mgmt-cosmosdb, azure-mgmt-sql, azure-mgmt-datalake-nspkg, azure-mgmt-datalake-store, azure-mgmt-datafactory, azure-mgmt-devspaces, azure-mgmt-cdn, azure-mgmt-rdbms, azure-mgmt-authorization, azure-mgmt-network, azure-mgmt-containerinstance, azure-mgmt-advisor, azure-mgmt-relay, azure-mgmt-compute, azure-mgmt-managementgroups, azure-mgmt-maps, azure-mgmt-servicebus, azure-mgmt-datalake-analytics, azure-mgmt-containerregistry, azure-mgmt-powerbiembedded, azure-mgmt-batch, azure-mgmt-devtestlabs, azure-mgmt-scheduler, azure-mgmt-managementpartner, azure-mgmt-iothubprovisioningservices, azure-mgmt-monitor, azure-mgmt-iotcentral, azure-mgmt-loganalytics, azure-mgmt-batchai, azure-mgmt-eventgrid, azure-mgmt, Click, Werkzeug, MarkupSafe, Jinja2, itsdangerous, Flask, WTForms, Flask-WTF, futures, scandir, pathlib2
            Running setup.py install for pycparser: started
              Running setup.py install for pycparser: finished with status 'done'
            Running setup.py install for scandir: started
              Running setup.py install for scandir: finished with status 'done'
          Successfully installed Click-7.0 Flask-1.0.3 Flask-WTF-0.14.2 Jinja2-2.10.1 MarkupSafe-1.1.1 PyJWT-1.7.1 WTForms-2.2.1 Werkzeug-0.15.4 adal-1.2.1 asn1crypto-0.24.0 azure-common-1.1.23 azure-mgmt-4.0.0 azure-mgmt-advisor-1.0.1 azure-mgmt-applicationinsights-0.1.1 azure-mgmt-authorization-0.50.0 azure-mgmt-batch-5.0.1 azure-mgmt-batchai-2.0.0 azure-mgmt-billing-0.2.0 azure-mgmt-cdn-3.1.0 azure-mgmt-cognitiveservices-3.0.0 azure-mgmt-commerce-1.0.1 azure-mgmt-compute-4.6.2 azure-mgmt-consumption-2.0.0 azure-mgmt-containerinstance-1.5.0 azure-mgmt-containerregistry-2.8.0 azure-mgmt-containerservice-4.4.0 azure-mgmt-cosmosdb-0.4.1 azure-mgmt-datafactory-0.6.0 azure-mgmt-datalake-analytics-0.6.0 azure-mgmt-datalake-nspkg-3.0.1 azure-mgmt-datalake-store-0.5.0 azure-mgmt-datamigration-1.0.0 azure-mgmt-devspaces-0.1.0 azure-mgmt-devtestlabs-2.2.0 azure-mgmt-dns-2.1.0 azure-mgmt-eventgrid-1.0.0 azure-mgmt-eventhub-2.6.0 azure-mgmt-hanaonazure-0.1.1 azure-mgmt-iotcentral-0.1.0 azure-mgmt-iothub-0.5.0 azure-mgmt-iothubprovisioningservices-0.2.0 azure-mgmt-keyvault-1.1.0 azure-mgmt-loganalytics-0.2.0 azure-mgmt-logic-3.0.0 azure-mgmt-machinelearningcompute-0.4.1 azure-mgmt-managementgroups-0.1.0 azure-mgmt-managementpartner-0.1.1 azure-mgmt-maps-0.1.0 azure-mgmt-marketplaceordering-0.1.0 azure-mgmt-media-1.0.0 azure-mgmt-monitor-0.5.2 azure-mgmt-msi-0.2.0 azure-mgmt-network-2.7.0 azure-mgmt-notificationhubs-2.1.0 azure-mgmt-nspkg-3.0.2 azure-mgmt-policyinsights-0.1.0 azure-mgmt-powerbiembedded-2.0.0 azure-mgmt-rdbms-1.9.0 azure-mgmt-recoveryservices-0.3.0 azure-mgmt-recoveryservicesbackup-0.3.0 azure-mgmt-redis-5.0.0 azure-mgmt-relay-0.1.0 azure-mgmt-reservations-0.2.1 azure-mgmt-resource-2.2.0 azure-mgmt-scheduler-2.0.0 azure-mgmt-search-2.1.0 azure-mgmt-servicebus-0.5.3 azure-mgmt-servicefabric-0.2.0 azure-mgmt-signalr-0.1.1 azure-mgmt-sql-0.9.1 azure-mgmt-storage-2.0.0 azure-mgmt-subscription-0.2.0 azure-mgmt-trafficmanager-0.50.0 azure-mgmt-web-0.35.0 azure-nspkg-3.0.2 certifi-2019.6.16 cffi-1.12.3 chardet-3.0.4 cryptography-2.7 enum34-1.1.6 futures-3.2.0 idna-2.8 ipaddress-1.0.22 isodate-0.6.0 itsdangerous-1.1.0 msrest-0.6.8 msrestazure-0.6.1 oauthlib-3.0.1 pathlib2-2.3.4 pycparser-2.19 python-dateutil-2.8.0 requests-2.22.0 requests-oauthlib-1.2.0 scandir-1.10.0 six-1.12.0 typing-3.7.4 urllib3-1.25.3
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
#0   running   2019-07-09T15:58:44Z   0.0%   1.8M of 512M   224K of 2G `


