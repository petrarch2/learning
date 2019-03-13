from PIL import Image
a = Image.open( 'Akha_cropped_hires.JPG' )    # 画像を読み込む
print( type( a ) )    # <class 'PIL.JpegImagePlugin.JpegImageFile'>　と表示される
a.save( 'piltest.png' )    # 画像を保存する
print( a.size[ 0 ] )    # 331　と表示される（幅）
print( a.size[ 1 ] )    # 554　と表示される（高さ）
print( a.info )    # 画像の情報を表示
"""
{'jfif': 257, 'jfif_version': (1, 1), 'dpi': (98, 98), 'jfif_unit': 1, 'jfif_density': (98, 98)}
と表示される
"""
import numpy
b = numpy.array( a )    # numpyのndarray型に変換する
c = Image.fromarray( b )    # numpyのndarray型から画像にする
from urllib import request
import io
with request.urlopen( 
	'https://upload.wikimedia.org/wikipedia/commons/6/68/Akha_cropped_hires.JPG'
		) as response:    # URLを開く
	buffer = response.read()    # ダウンロードしてバイト列にする
	d = Image.open( io.BytesIO( buffer ) )    # バイト列から画像を読み込む
e = a.convert( 'L' )     # グレースケール化する
e.save( 'pilmonotone.png' )
f, g, h = a.split()    # R,G,B各チャンネルからなる画像3枚を作成
i, j, k = a.convert( 'HSV' ).split()    # H,S,V各チャンネルからなる画像3枚を作成
j.save( 'pilsaturation.png' )    # 彩度のみからなる画像を保存
l = a.rotate( 45 )    # 45度回転
l.save( 'pilrotate.png' )    # 回転した画像を保存
m = a.rotate( 45, expand=True )    # 45度回転
m.save( 'pilexrotate.png' )    # 回転した画像を保存
from PIL import ImageOps
n = ImageOps.flip( a )    # 上下反転
n.save( 'pilflip.png' )    # 上下反転した画像を保存
o = ImageOps.mirror( a )    # 左右反転
o.save( 'pilmirror.png' )    # 左右反転した画像を保存
p = ImageOps.invert( a )    # 色を反転
p.save( 'pilinvert.png' )    # 色を反転した画像を保存
from PIL import ImageDraw

# 150×100サイズで背景が灰色の画像を作成
q = Image.new( 'RGB', ( 150, 100 ), ( 192, 192, 192 ) )
# 画像への描写を開始
r = ImageDraw.Draw( q )
# 線を引く
r.line( ( 5, 4, 95, 4 ), fill=( 255, 64, 0 ), width=1 )
r.line( ( 5, 8, 95, 8 ), fill=( 255, 128, 0 ), width=2 )
r.line( ( 5, 14, 95, 14 ), fill=( 255, 192, 0 ), width=4 )

# 扇状に線を引く
import math
for s in range( 0, 91, 10 ):
	t = s * math.pi / 180
	u = 100 + 45 * math.cos( t )
	v = 4 + 45 * math.sin( t )
	r.line( ( 100, 4, u, v ), fill=( 0, 255, 0 ), width=1 )

# 楕円を描写
r.ellipse( ( 5, 25, 50, 55 ), fill=( 255, 255, 0 ) )
# 輪郭線を付けて楕円を描写
r.ellipse( ( 5, 65, 50, 85 ), fill=( 255, 0, 0 ), outline=( 0, 0, 0 ) )

# 輪郭線を付けて矩形を描写
r.rectangle( ( 55, 25, 90, 90 ), fill=( 0, 192, 192 ), outline=( 255, 255, 255 ) )

# 文字列を描写
r.text( ( 100, 60 ), 'Hello,' )
r.text( ( 100, 80 ), 'World!', fill=( 0, 0, 0 ) )

# 画像を保存
q.save( 'pildraw.png' )
