a = []
a.append( 0 )
b = a
b.append( 1 )
print( a )    # [0, 1]　と表示される
c = []
c.append( 0 )
d = c.copy()
d.append( 1 )
print( c )    # [0]　と表示される
print( d )    # [0, 1]　と表示される
e = [ [] ]
e[0].append( 0 )
f = e.copy()
f[0].append( 1 )
print( e )    # [[0, 1]]　と表示される
import copy
g = [ [] ]
g[0].append( 0 )
h = copy.deepcopy( g )
h[0].append( 1 )
print( g )    # [[0]]　と表示される
print( h )    # [[0, 1]]　と表示される
