from lxml import etree

f = open("show_security_zones.xml")
foutput = f.read()
f.close()

xmlstruct = etree.fromstring(foutput)

first_zone = xmlstruct.find("zones-security")
print("Find tag of the first zones-security element")
print("---------------------")
print(first_zone.tag)

first_zone_children = first_zone.getchildren()

print("Find tag of all child elements of the first zones-security element")
print("---------------------")
for elem in first_zone_children:
    print(elem.tag)


