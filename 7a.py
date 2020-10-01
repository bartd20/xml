#import requests
#from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lxml import etree
from nxapi_plumbing import Device
from pprint import pprint

#requests.packages.urllib3.disable_warning(InsecureRequestWarning)

nxos1 = Device(
    api_format = "xml",
    host = "nxos1.lasthop.io",
    username = "pyclass",
    password = "PASSWORD",
    transport = "https",
    port = 8443,
    verify = False,
)

xmloutput = nxos1.show("show interface Ethernet1/1")
intf = xmloutput.find("body").find("TABLE_interface").find("ROW_interface")

print("Interface:")
print(intf.find("interface").text)
print("State:")
print(intf.find("state").text)
print("MTU:")
print(intf.find("eth_mtu").text)
