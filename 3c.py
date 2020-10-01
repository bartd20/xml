import xmltodict


def load_xml(fname,flist):
    
    f = open(fname)
    foutput = f.read()
    f.close()

    xmlout = xmltodict.parse(foutput,force_list={flist: True})

    return xmlout

#xml1 = load_xml("show_security_zones.xml")
xml2 = load_xml("show_security_zones_single_trust.xml","zones-security")

#print(type(xml1["zones-information"]["zones-security"]))
print(type(xml2["zones-information"]["zones-security"]))
