#from azure.common.client_factory import get_client_from_cli_profile
from azure.mgmt.compute import ComputeManagementClient
from azure.common.credentials import ServicePrincipalCredentials
#from azure.mgmt.compute.models import DiskCreateOption
from flask import Flask, render_template,  redirect, url_for,  request, flash
from forms import ContactForm

app = Flask(__name__)
app.secret_key = 'bojinawskey'

#SUBSCRIPTION_ID = 'ab23d036-20bc-4911-b398-31931d46c268'
GROUP_NAME = 'bojin'
LOCATION = 'eastus'
VM_NAME = 'bjin-py-vm'

@app.route('/')
def index():
   return redirect(url_for('login'))

@app.route('/login', methods = ['POST', 'GET'])
def login():
    form = ContactForm()
    
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('login.html', form = form)
        else:
            subscriptionid = form.subscriptionid.data
            CLIENT = form.clientid.data
            KEY = form.secret.data
            TENANT_ID = form.tenant.data
            print(CLIENT, KEY, TENANT_ID)
            get_credentials(CLIENT, KEY, TENANT_ID)
            awslogin(subscriptionid)
            return redirect(url_for('aws'))

    return render_template('login.html',  form = form)
   
@app.route('/aws', methods = ['POST', 'GET'])
def aws():
    vmlist = {}
    for v in EC2_CLIENT.virtual_machines.list_all():
        vmlist[v.name] = {}
        vm = EC2_CLIENT.virtual_machines.get(GROUP_NAME, v.name, expand='instanceView')
        vmlist[v.name]['computerName'] = vm.os_profile.computer_name
        vmlist[v.name]['location'] = vm.location
        for stat in vm.instance_view.statuses:
            vmlist[v.name]['displayStatus'] = stat.display_status
        print(vmlist)
    return render_template('azure.html', vmlist = vmlist)

def get_credentials(CLIENT, KEY, TENANT_ID):
    global CREDENTIALS
    CREDENTIALS = ServicePrincipalCredentials(
        client_id = CLIENT,
        secret = KEY,
        tenant = TENANT_ID
    )
    print(CREDENTIALS)
    return 
    
def awslogin(subscriptionid):
    global EC2_CLIENT
    EC2_CLIENT = ComputeManagementClient(CREDENTIALS, subscriptionid)
    print("ec2_client:")
    print(EC2_CLIENT)
    return

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug = True)
    
   
