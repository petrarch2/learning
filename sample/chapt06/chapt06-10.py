import cv2
a = cv2.CascadeClassifier( 'haarcascade_frontalface_default.xml' )

import glob
for b in glob.glob( 'movie_files/*.jpg' ):
	c = cv2.imread( b )
	d = a.detectMultiScale( c )
	for x, y, w, h in d:
		cv2.circle( c, ( x + w//2, y + h//2 ), w//2, ( 0, 255, 255 ), -1 )    # 円を描写する
		cv2.putText( c, '^_^', ( x, y + h//2 ),
			cv2.FONT_HERSHEY_PLAIN,
			1.5, ( 0, 0, 0 ), 5 )    # 文字列を描写する
	cv2.imwrite( b, c )

import ffmpeg
e = ffmpeg.input( 'movie_files/%d.jpg', r=30 ,f='image2' )    # 入力
f = ffmpeg.input( 'sound_test.mp4')    # 音声入力

import os
if os.path.isfile( 'movie_face.mov' ):
	os.remove( 'movie_face.mov' )    # ファイルがある場合は削除

g = ffmpeg.output( e, f, 'movie_face.mov' )    # 出力

ffmpeg.run( g, cmd='/usr/local/bin/ffmpeg' )    # 実行
