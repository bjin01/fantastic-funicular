from azure.mgmt.compute import ComputeManagementClient
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.network import NetworkManagementClient

from flask import Flask, render_template,  redirect, url_for,  request, flash
from forms import ContactForm

app = Flask(__name__)
app.secret_key = 'bojinawskey'

@app.route('/')
def index():
   return redirect(url_for('login'))

@app.route('/login', methods = ['POST', 'GET'])
def login():
    form = ContactForm()
    global GROUP_NAME
    global SUBSCRIPTION_ID
    
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('login.html', form = form)
        else:
            SUBSCRIPTION_ID = form.subscriptionid.data
            CLIENT = form.clientid.data
            KEY = form.secret.data
            TENANT_ID = form.tenant.data
            GROUP_NAME = form.group.data
            get_credentials(CLIENT, KEY, TENANT_ID)
            awslogin()
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
        vmlist[v.name]['public_ip'] = get_public_ip(v.name)
        for stat in vm.instance_view.statuses:
            vmlist[v.name]['displayStatus'] = stat.display_status
    return render_template('azure.html', vmlist = vmlist)

@app.route('/actions', methods = ['POST', 'GET'])
def actions():
    if request.method == 'POST':
        
        if request.form['actionsBtn'] == "Start":
            print(request.form['actionsBtn'])
            found_vm_list = request.form.getlist("found_vm")
            for i in found_vm_list:
                result = EC2_CLIENT.virtual_machines.start(GROUP_NAME, i)
                print(result)
            
        elif request.form['actionsBtn'] == "Stop":
            print(request.form['actionsBtn'])
            found_vm_list = request.form.getlist("found_vm")
            for i in found_vm_list:
                result = EC2_CLIENT.virtual_machines.power_off(GROUP_NAME, i)
                print(result)
            
        elif request.form['actionsBtn'] == "Deallocate":
            print(request.form['actionsBtn'])
            found_vm_list = request.form.getlist("found_vm")
            for i in found_vm_list:
                result = EC2_CLIENT.virtual_machines.deallocate(GROUP_NAME, i)
                print(result)
           
    return redirect(url_for('aws'))
    
def get_credentials(CLIENT, KEY, TENANT_ID):
    global CREDENTIALS
    CREDENTIALS = ServicePrincipalCredentials(
        client_id = CLIENT,
        secret = KEY,
        tenant = TENANT_ID
    )
    return 
    
def awslogin():
    global EC2_CLIENT
    EC2_CLIENT = ComputeManagementClient(CREDENTIALS, SUBSCRIPTION_ID)
    return
    
def get_public_ip( vmname):
    public_ip = []
    network_client = NetworkManagementClient(CREDENTIALS, SUBSCRIPTION_ID)
    public_ip_list = network_client.public_ip_addresses.list(GROUP_NAME)
    for x in public_ip_list:
        if vmname in x.id:
            public_ip.append(x.ip_address)
    return public_ip
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug = True)
    
   
