a = a = 'Hello' < 'Nice to meet you'
print( a )    # Trueと表示される
b = 'こんにちは' > 'こんばんは'
print( b )    # Falseと表示される
c = 3 in [ 0, 1, 2, 3 ]
print( c )    # Trueと表示される
d = 'e' in ( 'a', 'b', 'd', 'd' )
print( d )    # Falseと表示される
e = 'a' in 'Hello'
print( e )    # Falseと表示される
f = 'e' in 'Hello'
print( f )    # Trueと表示される
g = type( 'Hello' ) is str
print( g )    # Trueと表示される
h = type( 'Hello' ) is int
print( h )    # Falseと表示される
i = type( 0 ) is int
print( i )    # Trueと表示される
j = type( 0.0 ) is float
print( j )    # Trueと表示される
k = 'a' in 'Hello'
print( k )    # Falseと表示される
l = not 'a' in 'Hello'
print( l )    # Trueと表示される
m = 'a' not in 'Hello'
print( m )    # Trueと表示される
from numpy import nan
n = nan
print( n )    # nanと表示される
o = n == nan
print( o )    # Falseと表示される
p = nan == nan
print( p )    # Falseと表示される
q = n is nan
print( q )    # Trueと表示される
from numpy import inf
r = inf
print( r )    # infと表示される
s = r == inf
print( s )    # Trueと表示される
t = r is inf
print( q )    # Trueと表示される
u = inf is nan
print( u )    # Falseと表示される
from numpy import float32
v = float32(10) / float32(0)
print( v )    # infと表示される
w = float32(0) / float32(0)
print( w )    # nanと表示される
