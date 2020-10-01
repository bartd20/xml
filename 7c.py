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


cmds = (
    "interface loopback 110",
    "description loopback-110",
    "interface loopback 111",
    "description loopback-111"
)

output = nxos1.config_list(cmds)

for elem in output:
    print(etree.tostring(elem).decode())

