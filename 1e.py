from lxml import etree

f = open("show_security_zones.xml")
foutput = f.read()
f.close()

xmlstruct = etree.fromstring(foutput)

children = xmlstruct.getchildren()
trust_zone = children[0]

print(trust_zone[0].text)

for elem in trust_zone:
    print(elem)
    print(elem.tag)
    print("---")
