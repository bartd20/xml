from lxml import etree

f = open("show_security_zones.xml")
foutput = f.read()
f.close()

xmlstruct = etree.fromstring(foutput)

children = xmlstruct.getchildren()
# direct indices
print(children[0])
print(children[0].tag)

# getchildren() method
print(xmlstruct.getchildren()[0])
print(xmlstruct.getchildren()[0].tag)

