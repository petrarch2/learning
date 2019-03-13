import numpy
w = numpy.array( [ 0, 1, 2, 3 ] )    # リストからndarrayを作成
print( w )    # [0 1 2 3]　と表示される
x = numpy.array( [ [ 0, 1 ], [ 2, 3 ], [ 4, 5 ] ] )    # 二次元のndarrayを作成
print( x )
# [[0 1]
#  [2 3]
#  [4 5]]　と表示される
y = numpy.array( [ 0, 1, 2, 3 ], dtype=numpy.float32 )  # データ型を指定して作成
print( y )    # [0. 1. 2. 3.]　と表示される
z = numpy.zeros( (4,) )    # 1次元で長さ4のゼロ配列を作成
print( z )    # [0. 0. 0. 0.]　と表示される
aa = numpy.array( [ 0, 1, 2, 3 ] )
ab = numpy.array( [ 4, 5, 6, 7 ] )
ac = aa + ab    # 4次元のndarray同士の足し算
print( ac )    # [ 4  6  8 10]　と表示される
ad = aa + [ 1, 2, 3, 4]    # ndarrayとリストの足し算
print( ad )    # [1 3 5 7]　と表示される
ae = aa + 10    # ndarrayと数値の足し算
print( ae )    # [10 11 12 13]　と表示される
af = aa * 2    # ndarrayと数値のかけ算
print( af )    # [0, 2, 4, 6]　と表示される
ag = numpy.array( [ 6, 3, 4, 1, 9, 1, 8, 7, 0, 4, 1, 2, 5, 6, 8 ] )
ah = numpy.mean( ag )    # 平均
print( ah )    # 4.333333333333333と表示される
ai = numpy.median( ag )    # 中央値
print( ai )   # 4.0と表示される
aj = numpy.std( ag )    # 標準偏差
print( aj )   # 2.844097201026872と表示される
ak = numpy.var( ag )    # 分散
print( ak )   # 8.088888888888889と表示される
