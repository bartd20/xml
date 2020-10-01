import xmltodict


def load_xml(filename):
    
    f = open(filename)
    foutput = f.read()
    f.close()

    xmlout = xmltodict.parse(foutput)

    return xmlout

xml1 = load_xml("show_security_zones.xml")
xml2 = load_xml("show_security_zones_single_trust.xml")

print(type(xml1["zones-information"]["zones-security"]))
print(type(xml2["zones-information"]["zones-security"]))
