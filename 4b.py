from lxml import etree

f = open("show_security_zones.xml")
foutput = f.read()
f.close()

xmlstruct = etree.fromstring(foutput)

first_zone = xmlstruct.find("zones-security")
print(first_zone.find("zones-security-zonename").text)
