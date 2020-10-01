import xmltodict

f = open("show_security_zones.xml")
foutput = f.read()
f.close()

xmlout = xmltodict.parse(foutput)

zones = xmlout["zones-information"]["zones-security"]

for k, elem in enumerate(zones, 1):
    zone_name = elem["zones-security-zonename"]
    print("Security zone #"+str(k)+" "+zone_name)


