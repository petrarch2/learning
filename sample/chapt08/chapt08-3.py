from urllib import request

url = 'https://www.myurl.com/'

# URLから「Request」クラスを作成
rq = request.Request( url )

# クッキー情報のヘッダーを追加
rq.add_header( 'Cookie', 'NAME=COOKIEDATA' )

# URLを開く
with request.urlopen( rq ) as response:
	html = response.read().decode( 'utf-8' )
