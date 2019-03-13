from urllib import request

url = 'https://www.myurl.com/'

# POSTで送信するデータ
data = 'postdata=hoge'

# URLを開く
with request.urlopen( url, data=data.encode( 'utf-8' ) ) as response:
	html = response.read().decode( 'utf-8' )
