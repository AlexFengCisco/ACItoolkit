'''
Created on Jan 5, 2015

@author: AlexFeng
'''
from acitoolkit.acitoolkit import *
from credentials.credentials import *
"""
Create a tenant with a single EPG and assign it statically to 2 interfaces.
This is the minimal configuration necessary to enable packet forwarding
within the ACI fabric.
"""
# Create the Tenant
tenant = Tenant('CCB_New_Tenant')

# Create the Application Profile
app = AppProfile('AlexApp', tenant)

# Create the EPG
epg_web = EPG('Alex_EPG_Web', app)
epg_app = EPG('Alex_EPG_App', app)
epg_db = EPG('Alex_EPG_DB', app)


# Create a Context and BridgeDomain
context = Context('CCB_vrf', tenant)
bd = BridgeDomain('CCB_bd', tenant)
bd.add_context(context)

# Place the EPG in the BD
epg_web.add_bd(bd)
epg_app.add_bd(bd)
epg_db.add_bd(bd)

# Declare 2 physical interfaces ,contents interface type pod node slot port number
if1 = Interface('eth', '1', '101', '1', '1')
if2 = Interface('eth', '1', '101', '1', '2')
if3 = Interface('eth', '1', '101', '1', '3')


# Create VLAN 5 on the physical interfaces
vlan5_on_if1 = L2Interface('vlan5_on_if1', 'vlan', '5')
vlan5_on_if1.attach(if1)

vlan6_on_if2 = L2Interface('vlan6_on_if2', 'vlan', '6')
vlan6_on_if2.attach(if2)

vlan7_on_if3 = L2Interface('vlan7_on_if3', 'vlan', '7')
vlan7_on_if3.attach(if3)

# Attach the EPG to the VLANs
epg_web.attach(vlan5_on_if1)
epg_app.attach(vlan6_on_if2)
epg_db.attach(vlan7_on_if3)


subnet1=Subnet('subnet1',bd)
subnet1.set_addr('1.1.1.254/24')




subnet2=Subnet('subnet2',bd)
subnet2.set_addr('2.2.2.254/24')

contract_app= Contract('app_contract', tenant)
entry_app = FilterEntry('entry_app',
                     applyToFrag='no',
                     arpOpc='unspecified',
                     dFromPort='3306',
                     dToPort='3306',
                     etherT='ip',
                     prot='tcp',
                     sFromPort='1',
                     sToPort='65535',
                     tcpRules='unspecified',
                     parent=contract_app)

contract_db= Contract('db_contract', tenant)
entry_db = FilterEntry('entry_db',
                     applyToFrag='no',
                     arpOpc='unspecified',
                     dFromPort='1551',
                     dToPort='1551',
                     etherT='ip',
                     prot='tcp',
                     sFromPort='1',
                     sToPort='65535',
                     tcpRules='unspecified',
                     parent=contract_db)

epg_app.provide(contract_app)
epg_web.consume(contract_app)

epg_db.provide(contract_db)
epg_app.consume(contract_db)


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