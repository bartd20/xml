from lxml import etree

f = open("show_security_zones.xml")
foutput = f.read()
f.close()

xmlstruct = etree.fromstring(foutput)
xmlstring = etree.tostring(xmlstruct)
print(xmlstring.decode())
