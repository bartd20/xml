from lxml import etree

f = open("show_security_zones.xml")
foutput = f.read()
f.close()

xmloutput = etree.fromstring(foutput)
print(type(xmloutput))
print(xmloutput)

