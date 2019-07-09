#from azure.common.client_factory import get_client_from_cli_profile
from azure.mgmt.compute import ComputeManagementClient
from azure.common.credentials import ServicePrincipalCredentials
#from azure.mgmt.compute.models import DiskCreateOption
from azure.mgmt.network import NetworkManagementClient



GROUP_NAME = 'bojin'
LOCATION = 'eastus'
VM_NAME = 'bjin-py-vm'

SUBCRIPTION_ID = 'ab23d036-20bc-4911-b398-31931d46c268'
CLIENT = 'a6143998-a048-41cd-948a-dcf75edca234'
KEY = '82L69D?/FwPm_bR-h0fVYpHWiI.-0nWf'
TENANT_ID = '856b813c-16e5-49a5-85ec-6f081e13b527'

def getaws():

    for vm in COMPUTE_CLIENT.virtual_machines.list_all():
        print("VM Information for: \t")
        vm = COMPUTE_CLIENT.virtual_machines.get(GROUP_NAME, vm.name, expand='instanceView')
        print("  computerName: ", vm.os_profile.computer_name)
        print("  provisioningStatus: ", vm.provisioning_state)
        print("  name: ", vm.name)
        print("  type: ", vm.type)
        print("  location: ", vm.location)
        print("\nVM instance status")
        for stat in vm.instance_view.statuses:
            print("  displayStatus: ", stat.display_status)
        print("---------------------------------")

    return

#def get_credentials(client_id, secret,  tenant):
#    credentials = ServicePrincipalCredentials(client_id, secret, tenant)
#    return credentials
    
def awslogin(SUBCRIPTION_ID, CLIENT, KEY,  TENANT_ID):
    global COMPUTE_CLIENT
    #getlogin =  credentials(CLIENT, KEY, TENANT_ID)
    #        resource_group_client = ResourceManagementClient(getlogin, subscriptionid)
    #        network_client = NetworkManagementClient(getlogin, subscriptionid)
    COMPUTE_CLIENT = ComputeManagementClient(credentials, SUBCRIPTION_ID)
    print(COMPUTE_CLIENT)
    return
    
def get_public_ip(SUBCRIPTION_ID):
    networks = []
    network_client = NetworkManagementClient(credentials, SUBCRIPTION_ID)
    result_list = network_client.virtual_networks.list(GROUP_NAME )
    for i in result_list:
        print(i.name)
        networks.append(i.name)
    public_ip_list = network_client.public_ip_addresses.list(GROUP_NAME)
    for x in public_ip_list:
        print(x.id)
        print(x.ip_address)
        print(x.tags)
        print(x.ip_tags)
        print(x.dns_settings)
    
    return
    
if __name__ == "__main__":
    #print(subscriptionid, client_id, secret,  tenant)
    credentials = ServicePrincipalCredentials(
    client_id = CLIENT,
    secret = KEY,
    tenant = TENANT_ID
)
    awslogin(SUBCRIPTION_ID, CLIENT,  KEY, TENANT_ID)
    getaws()
    get_public_ip(SUBCRIPTION_ID)
