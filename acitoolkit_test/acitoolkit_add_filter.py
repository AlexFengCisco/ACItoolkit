'''
Created on Jan 5, 2015

@author: AlexFeng
'''
from acitoolkit.acitoolkit import *
from credentials.credentials import *

# Create the Tenant
tenant = Tenant('Alex_Tenant')

# Create the Application Profile

contract_web= Contract('web_contract', tenant)
entry_web = FilterEntry('entry_web',
                     applyToFrag='no',
                     arpOpc='unspecified',
                     dFromPort='80',
                     dToPort='80',
                     etherT='ip',
                     prot='tcp',
                     sFromPort='unspecified',
                     sToPort='unspecified',
                     tcpRules='unspecified',
                     parent=contract_web)

app = AppProfile('AlexApp', tenant)

# Create the EPG
epg_web = EPG('Alex_EPG_Web',app)


epg_web.provide(contract_web)

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