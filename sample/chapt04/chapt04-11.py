import pandas
import numpy
def plusthree( x ):
	return x + 3

f = pandas.DataFrame( [ [ 0, 'Jone', 18, 1000, 20],
	 [ 1, 'Mike', 22, 22000, 500],
	[ 2, 'Bob', 12, 550, 12],
	[ 3, 'Tone', 32, 6000, 80] ], columns=[
	'id', 'name', 'age', 'value', 'price' ] )
g = f[ 'age' ].map( plusthree )
print( g )
"""
0    21
1    25
2    15
3    35
Name: age, dtype: int64
と表示される
"""

h = f[ 'value' ].apply( plusthree )
print( h )
"""
0     1003
1    22003
2      553
3     6003
Name: value, dtype: int64
"""
i = f[ 'price' ].map( lambda x: x + 3 )
print( i )
"""
0     23
1    503
2     15
3     83
Name: price, dtype: int64
と表示される
"""
j = f[ 'name' ].map( {'Tone':'Tony', 'Bob':'Boby'} )
print( j )
"""
0     NaN
1     NaN
2    Boby
3    Tony
Name: name, dtype: object
と表示される
"""
def multithree( x ):
	return x * 3

k = f.applymap( multithree )
print( k )
"""
   id          name  age  value  price
0   0  JoneJoneJone   54   3000     60
1   3  MikeMikeMike   66  66000   1500
2   6     BobBobBob   36   1650     36
3   9  ToneToneTone   96  18000    240
と表示される
"""
f.apply( print )
"""
0    0
1    1
2    2
3    3
Name: id, dtype: object
0    Jone
1    Mike
2     Bob
3    Tone
Name: name, dtype: object
0    18
1    22
2    12
3    32
Name: age, dtype: object
0     1000
1    22000
2      550
3     6000
Name: value, dtype: object
0     20
1    500
2     12
3     80
Name: price, dtype: object
id       None
name     None
age      None
value    None
price    None
dtype: object
と表示される
"""
