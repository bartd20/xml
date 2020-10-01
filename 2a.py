import xmltodict

f = open("show_security_zones.xml")
foutput = f.read()
f.close()

xmlout = xmltodict.parse(foutput)
print(type(xmlout))
print(xmlout)


