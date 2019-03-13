import cv2
a = cv2.imread( 'Akha_cropped_hires.JPG' )    # 画像を読み込む
print( type( a ) )    # <class 'numpy.ndarray'>　と表示される
print( a.shape )    # (554, 331, 3)　と表示される
b = a[ 70:150, 100:200 ]
cv2.imwrite( 'cvtest.png', b )
import numpy
c = numpy.array([ [ [0,0,0], [255,255,255], [0,0,0] ],
		[ [255,255,255], [0,0,0], [255,255,255] ],
		[ [0,0,0], [255,255,255], [0,0,0] ] ],
		dtype=numpy.uint8 )
cv2.imwrite( 'cvtest2.png', c )
d = cv2.resize( c, ( 100, 100 ), interpolation=cv2.INTER_CUBIC )
cv2.imwrite( 'cvtest3.png', d,
	[ cv2.IMWRITE_PNG_COMPRESSION, 9 ]  )
e = a[ 70:150, 100:200 ]    # 部分画像を取得

f = cv2.medianBlur( e, ksize=5 )    # メディアンフィルタ
cv2.imwrite( 'cvmedian.png', f )

g = cv2.bilateralFilter( f, 5, 32, 32 )    # バイラテラルフィルタ
cv2.imwrite( 'cvbilateral.png', g )

h = cv2.fastNlMeansDenoisingColored( f )    # ノンローカルミーンフィルタ
cv2.imwrite( 'cvnonlocalmean.png', h )
i = numpy.array( [ [ 1/9, 1/9, 1/9 ], 
	[ 1/9, 1/9, 1/9 ], 
	[ 1/9, 1/9, 1/9 ] ] )    # 3x3の平均化カーネル
j = cv2.filter2D( e, -1, i )    # カーネルによるフィルター処理
cv2.imwrite( 'cvkernel.png', j )
k = cv2.cvtColor( a[ 70:150, 100:200 ], cv2.COLOR_RGB2GRAY )    # グレースケール画像を取得
l, m = cv2.threshold(k, 127, 255, 
	cv2.THRESH_BINARY )    # 閾値を指定して二値化
cv2.imwrite( 'cvthreshold.png', m )

n, o = cv2.threshold(k, 0, 255, 
	cv2.THRESH_BINARY + cv2.THRESH_OTSU )    # 大津メソッドで二値化
print( n )    # 101.0　と表示される（求められた閾値）
cv2.imwrite( 'cvotsu.png', o )
p = cv2.adaptiveThreshold( k, 255,
	cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
	cv2.THRESH_BINARY, 11, 2 )    # 適応的閾値で二値化
cv2.imwrite( 'cvadaptive.png', p )
q = a[ 70:150, 100:200 ]    # 部分画像を取得
r = cv2.pyrMeanShiftFiltering( q, 5, 32 )
cv2.imwrite( 'cvmeanshift.png', r )
s = q.reshape( ( -1, 3 ) ).astype( numpy.float32 )    # 画素を一列に並べる
"""
画素を量子化する
2番目の引数8は新しい色数、繰り返し数10回、精度1.0まで実行
"""
t, label, center=cv2.kmeans( s, 8, None,  
	(cv2.TERM_CRITERIA_MAX_ITER + cv2.TERM_CRITERIA_EPS, 10, 1.0),
	10, cv2.KMEANS_RANDOM_CENTERS )
"""
centerは新しい色、labelは新しい色へのインデックス
label[ :, 0 ]で新しい色へのインデックスの値を取得し、centerから色の並びを取得
"""
u = center[ label[ :, 0 ] ]
"""
色の並びを元の画像の形に戻してunit8型にすると減色処理が完了
"""
v = u.reshape( q.shape ).astype( numpy.uint8 )
cv2.imwrite( 'cvkmeans.png', v )
w = cv2.imread( 'cvtest.png', 0 )    # グレースケールで画像を読み込む
x = cv2.Sobel( w, cv2.CV_32F, 1, 0, ksize=3 )
cv2.imwrite( 'cvsobel.png', x )

y = cv2.Laplacian( w, cv2.CV_32F, ksize=3 )
cv2.imwrite( 'cvlaplacian.png', y )

z = cv2.Canny( w, 100, 200, aperture_size=3 ) # Opencvのバージョン3ではcv2.Canny( w, 100, 200 )とする
cv2.imwrite( 'cvcanny.png', z )
