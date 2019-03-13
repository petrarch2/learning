from urllib import request

url = 'https://www.myurl.com/'

import json

# POSTで送信するデータ
with open( 'sample.json', 'r' ) as f:
	data = json.loads( f.read() )    # dataにJSONデータが入る

# URLから「Request」クラスを作成
rq = request.Request( url )

# MIME情報のヘッダーを追加
rq.add_header( 'Content-type', 'application/json' )

# URLを開く
with request.urlopen( rq, data=data.encode( 'utf-8' ) ) as response:
	html = response.read().decode( 'utf-8' )
