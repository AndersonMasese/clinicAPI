from xml.dom import minidom

f = open('myCustomApiFile.txt', 'r')
pets = minidom.parseString(f.read())
f.close()

names = pets.getElementsByTagName('name')
for name in names:
	print (name.firstChild.nodeValue)