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

#print(etree.tostring(nxos1.show("show system uptime")).decode())
#print(etree.tostring(nxos1.show("show system resources")).decode())

cmds = (
    "show system uptime",
    "show system resources"
)

for elem in cmds:
    print(etree.tostring(nxos1.show(elem)).decode())
