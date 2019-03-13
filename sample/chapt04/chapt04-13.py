a = [ 6, 3, 4, 1, 9 ]
a.sort()
print( a )    # [1, 3, 4, 6, 9]　と表示される
b = [ 'Hello', 'Nice to meet you', 'How are you' ]
b.sort()
print( b )    # ['Hello', 'How are you', 'Nice to meet you']　と表示される
c = [ 6, 3, 4, 1, 9 ]
d = sorted( c )
print( c )    # [6, 3, 4, 1, 9]　と表示される
print( d )    # [1, 3, 4, 6, 9]　と表示される
reversed( [ 0, 1, 2, 3, 4 ] )     # これは、[4,3,2,1,0]と出力するイテレーターを返す
reversed( range( 0, 5, 1 ) )     # これは、4から0まで、1ずつ減るイテレーターを返す
reversed( range( 0, 5 ) )    # 上と同じ
reversed( range( 5 ) )     # 上と同じ
e = [ 'Hello', 'Nice to meet you', 'How are you' ]
f = reversed( sorted( e ) )    # fはイテレーター
print( f )    # <list_reverseiterator object at 0x7f97a2ec6b38>　と表示される
g = list( f )    # fをリストに変換
print( g )    # ['Nice to meet you', 'How are you', 'Hello']　と表示される
h = sorted( e )[ ::-1 ]    # hはeの逆順ソート結果のリストが入る
print( h )    # ['Nice to meet you', 'How are you', 'Hello']　と表示される
for i in range(10, 0, -1):
	print( i )
"""
10
9
8
7
6
5
4
3
2
1
と表示される
"""
for j in reversed( [ 1, 2, 3, 4, 5, 6 ] ):
	print( j )
"""
6
5
4
3
2
1
と表示される
"""
for k, l in [ (1, 2), (3, 4), (5, 6) ]:
	print( k, l )
"""
1 2
3 4
5 6　と表示される
"""
m = [ 10, 32, 55 ]
n = [ 'Hello', 'Nice to meet you', 'How are you' ]
o = list( zip( m, n ) )    # イテレーターをリストに変換してoに入れる
print( list( o ) )    # [(10, 'Hello'), (32, 'Nice to meet you'), (55, 'How are you')]　と表示される
for p, q in zip( m, n ):
	print( p, q )
"""
10 Hello
32 Nice to meet you
55 How are you
と表示される
"""
r = [ 'Hello', 'Nice to meet you', 'How are you' ]
for s, t in enumerate( r ):
	print( s, t )
"""
0 Hello
1 Nice to meet you
2 How are you
と表示される
"""
u = [ 10, 32, 55 ]
v = [ 'Hello', 'Nice to meet you', 'How are you' ]
for w, ( x, y ) in enumerate( zip( u, v ) ):
	print( w, x, y )
"""
0 10 Hello
1 32 Nice to meet you
2 55 How are you
と表示される
"""
import itertools
for z in itertools.count(0):
	print( z )
"""
0
1
2
・・・と表示される
"""
z = 0
while True:
	print( z )
	z += 1
