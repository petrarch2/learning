from urllib import request

url = 'https://www.myurl.com/'

# 「HTTPPasswordMgr」クラス作成する
passwd = request.HTTPPasswordMgr()
passwd.add_password( None, url, 'Username', 'Password' )

# オプションを作成してインストール
opn = request.build_opener( passwd )
request.install_opener( opn )

# URLを開く
with request.urlopen( url ) as response:
	html = response.read().decode( 'utf-8' )
