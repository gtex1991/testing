#Mend project
#Gaston

import urllib
import requests
import urllib.parse

'''
try:
	url = 'https://www.senate.gov/general/contact_information/senators_cfm.xml'

	headers = {}
	headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'

	req = urllib.request.Request(url, headers=headers)
	resp = urlliv.request.urlopen(req)
	respData = resp.read()

	saveFile = open('withHeaders.txt', 'w')
	saveFile.write(str(respData))
	saveFile.close()

exception Exception as e:
	print (str(e))
	'''
'''
r = requests.get('https://www.senate.gov/general/contact_information/senators_cfm.xml')
print r.status_code

r.headers['content-type']
'application/json; charset=utf8'

r.encoding
'utf-8'

'''

url = 'https://api.spotify.com/v1/search?type=artist&q=snoop'
f = urllib.request.urlopen(url)
print(f.read().decode('utf-8'))



