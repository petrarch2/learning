from urllib import request

url = 'https://www.myurl.com/'

try:
	# URLを開く
	with request.urlopen( rq ) as response:
		html = response.read().decode( 'utf-8' )
except URLError as e:    # URLに到達できない
	print( e.reason )    # エラーを表示
except HTTPError as e:    # HTTPレスポンスエラー
	print( e.code )    # HTTPステータスコードを表示
	print( e.reason )    # エラーを表示
except ContentTooShortError as e:    # ダウンロードが途中で止まった
	print( e.msg )    # エラーを表示
	print( len( e.content ) )    # ダウンロード出来た長さを表示
