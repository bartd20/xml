from lxml import etree

f = open("show_version.xml",mode="rb")
foutput = f.read()
f.close()

xmloutput = etree.fromstring(foutput)
print(xmloutput.nsmap)

