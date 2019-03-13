import ffmpeg
import os

a = ffmpeg.input( '../chapt06/Dancing_of_Zaza.ogv' )    # 入力

if os.path.isfile( 'movie_test.mov' ):
	os.remove( 'movie_test.mov' )    # ファイルがある場合は削除

b = ffmpeg.output( a, 'movie_test.mov', t=5, ss=20 )    # 出力

ffmpeg.run( b, cmd='/usr/local/bin/ffmpeg' )    # 実行

c = ffmpeg.input( 'movie_test.mov' )    # 入力

if os.path.isfile( 'sound_test.mp4' ):
	os.remove( 'sound_test.mp4' )    # ファイルがある場合は削除

d = ffmpeg.output( c, 'sound_test.mp4', map='0:1' )    # 出力

ffmpeg.run( d, cmd='/usr/local/bin/ffmpeg' )    # 実行

e = ffmpeg.input( 'movie_test.mov' )    # 入力

import shutil
if os.path.isdir( 'movie_files' ):
	shutil.rmtree( 'movie_files' )    # ディレクトリがある場合は削除
os.mkdir( 'movie_files' )    # 保存先ディレクトリの用意

f = ffmpeg.output( e, 'movie_files/%d.jpg', r=30 ,f='image2' )    # 出力

ffmpeg.run( f, cmd='/usr/local/bin/ffmpeg' )    # 実行

import cv2
a = cv2.CascadeClassifier( '../chapt06/haarcascade_frontalface_default.xml' )

# 一枚画像ファイルを処理する関数
def p( b ):
	c = cv2.imread( b )
	d = a.detectMultiScale( c )
	for x, y, w, h in d:
		cv2.circle( c, ( x + w//2, y + h//2 ), w//2, ( 0, 255, 255 ), -1 )    # 円を描写する
		cv2.putText( c, '^_^', ( x, y + h//2 ),
			cv2.FONT_HERSHEY_PLAIN,
			1.5, ( 0, 0, 0 ), 5 )    # 文字列を描写する
	cv2.imwrite( b, c )

# プロセスを作成する
import multiprocessing
a = multiprocessing.Pool( 4 )

# 並列処理で全てのファイルを処理する
import glob
a.map( p, glob.glob( 'movie_files/*.jpg' ) )

import ffmpeg
e = ffmpeg.input( 'movie_files/%d.jpg', r=30 ,f='image2' )    # 入力
f = ffmpeg.input( 'sound_test.mp4')    # 音声入力

import os
if os.path.isfile( 'movie_face.mov' ):
	os.remove( 'movie_face.mov' )    # ファイルがある場合は削除

g = ffmpeg.output( e, f, 'movie_face.mov' )    # 出力

ffmpeg.run( g, cmd='/usr/local/bin/ffmpeg' )    # 実行
