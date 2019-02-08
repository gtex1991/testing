import os
from xml.etree import ElementTree
import xml.etree.ElementTree as ET

'''
file_name = 'xmlRawData.xml'
full_file = os.path.abspath(os.path.join('data',file_name))
print (full_file)

dom = ElementTree.parse(full_file)

members = dom.findall('member/member_full')

for c in members:
	print (c.text)
'''


R= ElementTree.parse('xml_Rawdata2.xml') # import the data into the program
root = R.getroot()
#print (root)	#test

contact_information = R.findall('member')
addresses = R.findall('address')

for x in contact_information:
	'''
	firstName = x.find('first_name')
	lastName = x.find('last_name').text
	fullName = x.find('member_full').text

	print ('{')
	print (firstName)
	print (lastName)
	print (fullName)
	print ('}')
	'''
	
	
	print ('{')
	print ('\n')

	print ('\t','firstName:', '"', x.find('first_name').text,'"',)
	print ('\t','lastName:', '"',x.find('last_name').text,'"',)
	print ('\t','fullName:', '"',x.find('member_full').text,'"',)
	print ('\t','chartId:', '"',x.find('bioguide_id').text,'"',)
	print ('\t','mobile:', '"',x.find('phone').text,'"',)
	print ('\t','"address: " [ \n',
		'\t','{\n'
		'\t','\t','\t','"street: "\n',
		'\t','\t','\t','"city: "\n',
		'\t','\t','\t','"state: "\n',
		'\t','\t','\t','"postal: "\n',
		'\t','\t',']','\n'
		'\t','}\n')
	print ('\t','address:', '"',x.find('address').text,'"',)

	print ('}')

	address_str = (x.find('address').text,)
	str_add = ' '.join(address_str)
	print (str_add)

	for y in str_add:
		
		print (y)
	

#for child in root:
#	print (child.tag, child.attrib)
