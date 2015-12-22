'''
Created on Jan 5, 2015

@author: AlexFeng
'''
from acitoolkit.acitoolkit import *
from credentials.credentials import *

# Create the Tenant
tenant = Tenant('CCB_New_Tenant')

# Create the Application Profile
tenant.mark_as_deleted()

# Login to APIC and push the config
session = Session(URL, LOGIN, PASSWORD)
session.login()
resp = session.push_to_apic(tenant.get_url(), data=tenant.get_json())
if resp.ok:
    print 'Success'

# Print what was sent
print 'Pushed the following JSON to the APIC ..DELETE TENANT ALEX'
print 'URL:', tenant.get_url()
print 'JSON:', tenant.get_json()

if __name__ == '__main__':
    pass