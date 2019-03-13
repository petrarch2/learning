import ffmpeg
import os

a = ffmpeg.input( 'Dancing_of_Zaza.ogv' )    # 入力

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
