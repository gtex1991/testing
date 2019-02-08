import urllib
import urllib.request
import urllib.parse
import requests


'''
try:
    x = urllib.request.urlopen('https://www.google.com/search?q=test')
    print(x.read())

except Exception as e:
    print(str(e))
'''

'''
url = 'https://pythonprogramming.net/'
values = {'s':'basic',
 			'submit':'search'
}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)
respData = resp.read()

print (respData)

'''

'''
try:
	x = urllib.request.urlopen('http://www.google.com/search?q=test')

	print (x.read())
except Exception as e:
	print(str(e))
'''



try:
	url = 'http://ws.audioscrobbler.com/2.0/'

	headers = {}
	headers['User-Agents'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
	req = urllib.request.Request(url,headers = headers)
	resp = urllib.request.urlopen(req)
	respData = resp.read()
	print (respData)
	#print (respData.decode('utf-8'))

	saveFile= open('withHeaders.txt', 'w')
	saveFile.write(str(respData))
	saveFile.close()

except Exception as e:
	print (str(e))