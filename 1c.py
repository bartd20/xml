from lxml import etree

f = open("show_security_zones.xml")
foutput = f.read()
f.close()

xmlstruct = etree.fromstring(foutput)

# print root tag
print(xmlstruct.tag)

# print children type 
print(type(xmlstruct.getchildren()))

# print children number
print(len(xmlstruct.getchildren()))

