from lxml import etree

f = open("show_security_zones.xml")
foutput = f.read()
f.close()

xmlstruct = etree.fromstring(foutput)

zones = xmlstruct.findall("zones-security")

for elem in zones:
    print("zone-security-zonename:")
    print(elem.find("zones-security-zonename").text)


