import parser
import json
import xml.etree.ElementTree as ET
import xmltodict


# string object that contains the xml RAW Data from the API
'''
input = 
<stuff>
	<users>
		<user x= "2">
			<id>001</id>
			<name>Chuck</name>
		</user>
		<user x= "7">
			<id>009</id>
			<name>Brent</name>
		</user>
	</users>
</stuff>


stuff = ET.fromstring(input) # parse in the string, it returns a tree
lst = stuff.findall('users/user')
print ('User count:', len(lst))
for item in lst:
	print ('Name', item.find('name').text)
	print ('id', item.find('id').text)
	print ('attribute', item.get("x"))
'''
contact_information = '''
<contact_information>
	<member>
		<first_name>hello</first_name>
		<last_name>hello</last_name>
		<member_full>hello</member_full>
		<bioguide_id>hello</bioguide_id>
		<phone>hello</phone>

		<address>11223 444</address>
	</member>
</contact_information>
'''


print (contact_information)

contact_information = ET.fromstring(contact_information) # parse in the string, it returns a tree
lst2 = contact_information.findall('member')

for x in lst2:
	print ('{')
	print ('\n')
	print ('\t','firstName:', '"', x.find('first_name').text,'"',)
	print ('\t','lastName:', '"',x.find('last_name').text,'"',)
	print ('\t','fullName:', '"',x.find('member_full').text,'"',)
	print ('\t','chartId:', '"',x.find('bioguide_id').text,'"',)
	print ('\t','mobile:', '"',x.find('phone').text,'"',)
	print ('\t','address:', '"',x.find('address').text,'"',)

	print ('}')




