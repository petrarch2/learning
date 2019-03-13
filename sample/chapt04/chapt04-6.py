a = [ 1, 2, 3 ]    # リストを作成
b = [ 4, 5, 6 ]    # リストを作成
c = a + b    # リスト同士の＋演算は結合
print( c )    # [1, 2, 3, 4, 5, 6]　と表示される
import numpy
d = numpy.array( [ 1, 2, 3 ] )    # ndarray型を作成
e = numpy.array( [ 4, 5, 6 ] )    # ndarray型を作成
f = d + e    # ndarray同士の＋演算は加算
print( f )    # [5 7 9]　と表示される
# g = a + 3    # エラー
h = d + 3    # 値の加算
print( h )    # [4 5 6]　と表示される
i = [ 1, 2, 3 ]
j = i * 3
print( j )    # [1, 2, 3, 1, 2, 3, 1, 2, 3]　と表示される
k = numpy.array( [ 1, 2, 3 ] )
l = k * 3
print( l )    # [3 6 9]　と表示される 
# m = i * [ 1, 2, 3 ]    # エラー
n = k * numpy.array( [ 1, 2, 3 ] )    # 値の乗算
print( n )    # [1 4 9]　と表示される
o = [ [ 1, 2, 3 ], [ 4, 5, 6 ] ]
p = numpy.array( [ [ 1, 2, 3 ], [ 4, 5, 6 ] ] )
print( o[0][2] )    # 3　と表示される
print( p[0][2] )    # 3　と表示される
q = [ [ 1, 2 ], [ 3, 4, 5 ], [ 6 ] ]
r = numpy.array([ [ 1, 2 ], [ 3, 4, 5 ], [ 6 ] ] )
print( q[1][0] )    # 3　と表示される
print( r[1][0] )    # 3　と表示される
print( q )    # [[1, 2], [3, 4, 5], [6]]　と表示される
print( r )    # [list([1, 2]) list([3, 4, 5]) list([6])]　と表示される
print( p.shape )    # (2, 3)　と表示される
print( r.shape )    # (3,)　と表示される
print( p.dtype )    # int64　と表示される
print( r.dtype )    # object　と表示される
print( type( p[ 0 ] ) )    # <class 'numpy.ndarray'>　と表示される
print( type( r[ 0 ] ) )    # <class 'list'>　と表示される
s = p.mean()    # s = 3.5　となる
# t = r.mean()    # エラー
u = p.sum()    # u = 21　となる
v = r.sum()    # v = [1, 2, 3, 4, 5, 6]　となる
