#!/usr/bin/python3

import sys
import io
sys.stdout = io.TextIOWrapper( sys.stdout.buffer, encoding='utf-8' )

# データ型を定義する
class Tile:
	
	def __init__( self, word ):
		self.w = word
		self.right = None
		self.bottom = None
	
	# += 演算子のオーバーロード
	def __iadd__( self, val ):
		bef = None
		for w in reversed( val ):
			t = Tile( w )
			t.right = bef
			bef = t
		self.right = bef
		return self
		
	# *= 演算子のオーバーロード
	def __imul__( self, val ):
		bef = None
		for w in reversed( val ):
			t = Tile( w )
			t.bottom = bef
			bef = t
		self.bottom = bef
		return self

# CGIパラメーターを取得する
import cgi
param = cgi.FieldStorage()
cmd = ''
if 'cmd' in param:
	cmd = param[ 'cmd' ].value
if cmd.startswith( 'add' ):
	# タイルの追加なら場所と単語の2文字目以降を取得
	ax = int( param[ 'x' ].value )
	ay = int( param[ 'y' ].value )
	am = param[ 'm' ].value[ 1: ]

# クッキーを発行する
import os
from http import cookies

# 現在のクッキーを取得
cookie = cookies.SimpleCookie()
if 'HTTP_COOKIE' in os.environ:
	cookie.load( os.environ[ 'HTTP_COOKIE' ] )
# 無ければ新しく作成
import uuid
if 'GAME' not in cookie:
	cookie[ 'GAME' ] = uuid.uuid1()    # セッションIDを作成
gid = cookie[ 'GAME' ].value    # セッションIDを取得

# データベースに接続
import sqlite3
db = sqlite3.connect( '/var/db/game.db' )
cur = db.cursor()
# テーブルが無ければ作成
cur.execute( 'CREATE TABLE IF NOT EXISTS tile (id TEXT, val TEXT)' )
# セッションIDのデータを取得
cur.execute( 'SELECT val FROM tile WHERE id=?', ( gid, ) )
val = cur.fetchone()

# データベースの処理
import pickle
import base64

if not val:
	# データベースにセッションがなかったら、新しく盤面データを作成
	root = Tile( 'A' )
	root += 'LICE'    # 横に「ALICE」というタイル
	b = pickle.dumps( root )    # データを直列化
	s = base64.b64encode( b ).hex()    # Base64で文字列化
	# データベースにセッションの盤面データを追加
	cur.execute( 'INSERT INTO tile VALUES (?, ?)', ( gid, s ) )
elif cmd == 'end':
	# ゲームの終了ならデータベースから削除
	cur.execute( 'DELETE FROM tile WHERE id=?', ( gid, ) )
	root = None
else:
	# データベースから読み込む
	s = bytes.fromhex( val[ 0 ] )    # Base64バイト列
	b = base64.b64decode( s )    # 直列化データ
	root = pickle.loads( b )    # 盤面データを復元

# 再帰関数でタイルを追加する
def addtile( node=root, x=1, y=1 ):
	if not node:
		return None
	# コマンドと位置で追加する場所を判断
	if cmd == 'addr' and x == ax and y == ay:
		node += am  # 横に追加
	elif cmd == 'addb' and x == ax and y == ay:
		node *= am  # 縦に追加
	node.right = addtile( node.right, x+1, y )    # 再帰
	node.bottom = addtile( node.bottom, x, y+1 )    # 再帰
	return node    # 現在のタイルを返す

root = addtile()  # タイルを追加

# 新しい盤面をデータベースに保存
b = pickle.dumps( root )
s = base64.b64encode( b ).hex()
cur.execute( 'UPDATE tile SET val=? WHERE id=?', ( s, gid ) )

# データベースを更新して閉じる
db.commit()
db.close()

# 再帰関数で盤面をHTML化する
def gettile( node=root, x=1, y=1, c='addb' ):
	if not node:
		return ''
	# HTMLタグの文字列を返す
	return """
	<em style="left:%d;top:%d"
	    onclick="location.href='game.py?cmd=%s&x=%d&y=%d&m='+prompt()">
	%s
	</em>
	%s
	%s
	""" % ( x*50, y*50, c, x, y, node.w,    # タイルの表示内容
		gettile( node.right, x+1, y, 'addb' ),    # 再帰
		gettile( node.bottom, x, y+1, 'addr' ) )    # 再帰

# 表示するHTML
html = """
<html>
<head>
<style>
em {
  position: absolute;
  display: block;
  border: solid 1px black;
  width: 48px;
  height: 48px;
  background: silver;
  margin: 0;
  padding: 0;
}
</style>
</head>
<body>
<a href='game.py?cmd=end'>ゲームを終わる</a>
%s
</body>
</html>
"""

# HTTPヘッダーを送信
print( 'Content-Type: text/html' )
if cmd == 'end':
	# ゲームの終わりならクッキーを削除
	print( 'Set-Cookie: GAME=; expires=Thu, 1-Jan-1970 00:00:00 GMT;' )
else:
	# そうでなければクッキーを送信
	print( cookie )
# 1行空行を送信
print()
# HTMLに盤面を入れて送信
print( html % gettile() )

