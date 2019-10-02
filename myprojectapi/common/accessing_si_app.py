import urllib
from urllib import request

data = {'principle_amount' : 15000.0,
        'period' : 5,
        'rate' : 8}
data = urllib.parse.urlencode(data)
data = data.encode('ascii')

request1 = request.Request('http://127.0.0.1:5000/simpleinterest/', method='POST', data=data)
try:
    response1 = request.urlopen(request1)
    print(response1.read())
except urllib.error.HTTPError as e:
    print(e.code, e.read())