import xml.etree.ElementTree as ET
from collections import defaultdict
tree = ET.parse('CHARGES_PDC.xml')
root = tree.getroot()
Moc1=root.findall('chargeRatePlan')
dict=defaultdict(list)
for moc in Moc1:
    for node in moc.getiterator():
			if node.tag=='name':
				n=node.text
		
			if node.tag=='internalId':
				inid=node.text
				#print("internal id is" + inid)
				dict[str(n)].append(inid)
		
		
		
		
for i in dict:
	print i