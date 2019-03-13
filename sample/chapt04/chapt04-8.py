import pandas
r = pandas.Series([ 6, 3, 4, 1, 9, 1, 8, 7, 0, 4, 1, 2, 5, 6, 8 ])
print( r[ r == 6 ].values )    # [6 6]　と表示される
print( r[ r == 6 ].index )    # Int64Index([0, 13], dtype='int64')　と表示される
s = [ 6, 3, 4, 1, 9, 1, 8, 7, 0, 4, 1, 2, 5, 6, 8 ]
t = [ u for u in s if u > 3 ]    # sの3より大きい値のみからなるリスト
print( t )    # [6, 4, 9, 8, 7, 4, 5, 6, 8] と表示される
v = pandas.Series([ 6, 3, 4, 1, 9, 1, 8, 7, 0, 4, 1, 2, 5, 6, 8 ])
w = list( v[ v > 3 ].index )    # vの3より大きい値の位置をリストに
print( w )    # [0, 2, 4, 6, 7, 9, 12, 13, 14]　と表示される
x = v[ v > 3 ].values    # xはnumpyのndarray型
print( x )    # [6 4 9 8 7 4 5 6 8]　と表示される
