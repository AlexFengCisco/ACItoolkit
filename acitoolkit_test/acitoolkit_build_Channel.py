'''
Created on Jan 5, 2015

@author: AlexFeng
'''
from acitoolkit.acitoolkit import *
from credentials.credentials import *

# Create the Tenant
tenant = Tenant('Alex_Tenant')

# Create the Application Profile

intf1 = Interface('eth','1','102','1','4')
intf2 = Interface('eth','1','102','1','5')
intf3 = Interface('eth','1','101','1','4')
intf4 = Interface('eth','1','101','1','5')

# Create a port channel and add physical interfaces
pc = PortChannel('pc1')
pc.attach(intf1)
pc.attach(intf2)
pc.attach(intf3)
pc.attach(intf4)

# Create a VLAN interface on the port channel
# This is the L2 interface representing a single VLAN encap
# on this particular interface.
vlan8_on_pc = L2Interface('vlan8_on_pc', 'vlan', '8')
vlan8_on_pc.attach(pc)



# Create a tenant, app profile, and epg

app = AppProfile('AlexApp', tenant)
epg_ectip = EPG('ECTIP', app)

# Connect EPG to the VLAN interface
# Remember, this VLAN interface is on the port channel we created
# so the EPG will be attached to the port channel on VLAN 5
epg_ectip.attach(vlan8_on_pc)

# Print the resulting JSON
print pc.get_json()
print tenant.get_json()



# Login to APIC and push the config
session = Session(URL, LOGIN, PASSWORD)
session.login()
resp = session.push_to_apic(tenant.get_url(), data=tenant.get_json())
if resp.ok:
    print 'Success'

# Print what was sent
print 'Pushed the following JSON to the APIC'
print 'URL:', tenant.get_url()
print 'JSON:', tenant.get_json()


if __name__ == '__main__':
    pass