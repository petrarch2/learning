from urllib import request

url = 'https://www.myurl.com/'

# URLを開く
with request.urlopen( url ) as response:
	html = response.read().decode( 'utf-8' )
