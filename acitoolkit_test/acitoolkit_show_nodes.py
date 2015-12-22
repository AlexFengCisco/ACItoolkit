'''
Created on Jan 5, 2015

@author: AlexFeng
'''

from acitoolkit.acitoolkit import Session,Tenant
from acitoolkit.aciphysobject import Node,Link,Powersupply
from acitoolkit.acibaseobject import BaseACIObject
from credentials.credentials import *


# Take login credentials from the command line if provided
# Otherwise, take them from your environment variables file ~/.profile


# Login to APIC
session = Session(URL, LOGIN, PASSWORD)
session.login()



# List of classes to get and print
phy_class = (Node)
Phy_links=(Link)
Phy_pwrs=(Powersupply)

    # Get and print all of the items from the APIC
items = phy_class.get(session)
for item in items:
    print item.info()
    
links=Phy_links.get(session)

for link in links:
    print link.info() 
    
pwrs=Phy_pwrs.get(session)
for pwr in pwrs:
    print pwr.info()
        


for node in Node.get(session):
    print node.info()
    
tenant = Tenant('Alex_Tenant')    
    
res=session.get(tenant.get_url())
print res.text



if __name__ == '__main__':
    pass