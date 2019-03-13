import random
import re
from urllib import request
from bs4 import BeautifulSoup

url = 'https://www.wikipedia.org/'

while True:
	with request.urlopen( url ) as response:
		html = response.read().decode( 'utf-8' )
		soup = BeautifulSoup( html )
		print( soup.title.text )
now_url = url
while now_url == url:
	link = random.choice( soup.find_all( 'a' ) )
	href = link.get( 'href' )
	if href and ( href.endswith( '/' ) or href.endswith( '.html' ) ):
		if href.startswith( '//' ):
			url = 'https:' + href
		elif href.startswith( '/' ):
			host = response.geturl().split( '/' )[2]
			url = 'https://' + host + href
		else:
			url = href
		if not re.match( 'https://[a-z]*.wikipedia.org/', url ):
			url = now_url
