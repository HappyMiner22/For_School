from urllib import request

url = 'https://example.com'
req = request.Request(url)
response = request.urlopen(req)

print(req)