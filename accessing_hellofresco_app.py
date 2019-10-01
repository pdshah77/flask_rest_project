import urllib2
req = urllib2.Request('http://127.0.0.1:5000/')
try:
	response1 = urllib2.urlopen(req)
	print(response1.read())
	print('STATUS :',response1.status)
	print(response1.info())

except urllib2.HTTPError as e:
	print(e.code,e.read())