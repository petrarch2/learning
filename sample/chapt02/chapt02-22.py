def plusthree( x ):
	return x + 3

a = [ 1, 2, 3, 4 ]
b = map( plusthree, a )
for c in b:
	print( c )
"""
4
5
6
7
と表示される
"""
d = list( map( plusthree, a ) )
print( d )    # [4, 5, 6, 7]　と表示される
e = list( map( str, a ) )
print( e )    # ['1', '2', '3', '4']　と表示される
f = map( plusthree, a )
g = list( f )
print( g )    # [4, 5, 6, 7]　と表示される
h = list( f )
print( h )    # []　と表示される
