from urllib import request

url = 'http://yahoo.co.jp'

with request.urlopen( url ) as response:
	# URLから読み込む
	html = response.read().decode( 'utf-8' )

from urllib.error import URLError, HTTPError

try:
	with request.urlopen( url ) as response:
		# URLから読み込む
		html = response.read().decode( 'utf-8' )
except URLError as e:
	print( '接続エラー' )    # エラー発生時
except HTTPError as e:
	print( '通信エラー' )    # エラー発生時
