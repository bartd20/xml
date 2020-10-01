#import requests
#from requests.packages.urllib3.exceptions import InsecureRequestWarning
from nxapi_plumbing import Device
from pprint import pprint

#requests.packages.urllib3.disable_warning(InsecureRequestWarning)

nxos1 = Device(
    api_format = "jsonrpc",
    host = "nxos1.lasthop.io",
    username = "pyclass",
    password = "PASSWORD",
    transport = "https",
    port = 8443,
    verify = False,
)

output = nxos1.show("show interface Ethernet1/1")
print("Interface:")
print(output["TABLE_interface"]["ROW_interface"]["interface"])
print("State:")
print(output["TABLE_interface"]["ROW_interface"]["state"])
print("MTU:")
print(output["TABLE_interface"]["ROW_interface"]["eth_mtu"])
