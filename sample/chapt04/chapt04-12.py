import pandas
import numpy
l = pandas.DataFrame( [ [ 0, 'Jone', 18, 1000, 20],
	 [ 1, 'Mike', 22, 22000, 500],
	[ 2, 'Bob', 12, 550, 12],
	[ 3, 'Tone', 32, 6000, 80] ], columns=[
	'id', 'name', 'age', 'value', 'price' ] )
m = l.iloc[1:3]    # スライスで表の一部を取り出す
print( m )
"""
   id  name  age  value  price
1   1  Mike   22  22000    500
2   2   Bob   12    550     12
と表示される
"""

n = l[ [ 'value', 'price' ] ] + 3    # 一部を取り出して3を加えた表を作成
print( n )
"""
   value  price
0   1003     23
1  22003    503
2    553     15
3   6003     83
と表示される
"""

o = l[ [ 'name', 'age' ]].iloc[3:]    # ラベルとスライスを組み合わせる
print( o )
"""
   name  age
3  Tone   32
と表示される
"""

p = l.copy()    # lのコピーを作成する
q = pandas.DataFrame( [[ 'Alice', 10, 4, 100000, 1000 ]],
	columns=[ 'name', 'age', 'id', 'value', 'price' ] )
r = l.append( q )    # lにqを追加する
print( r )
"""
   age  id   name  price   value
0   18   0   Jone     20    1000
1   22   1   Mike    500   22000
2   12   2    Bob     12     550
3   32   3   Tone     80    6000
0   10   4  Alice   1000  100000
と表示される（インデックス0が重複）
"""

s = l.append( q, ignore_index=True )    # lにqを追加する
print( s )
"""
   age  id   name  price   value
0   18   0   Jone     20    1000
1   22   1   Mike    500   22000
2   12   2    Bob     12     550
3   32   3   Tone     80    6000
4   10   4  Alice   1000  100000
と表示される（インデックスが振り直された）
"""

r = pandas.concat( [ l, q ] )    # 縦方向に結合
print( r )
"""
   age  id   name  price   value
0   18   0   Jone     20    1000
1   22   1   Mike    500   22000
2   12   2    Bob     12     550
3   32   3   Tone     80    6000
0   10   4  Alice   1000  100000
と表示される
"""

s = pandas.DataFrame( [ 10, 110, 5.5, 60 ], columns=[ 'tax' ] )
t = pandas.concat( [ l, s ], axis=1 )    # 横方向に結合
print( t )
"""
   id  name  age  value  price    tax
0   0  Jone   18   1000     20   10.0
1   1  Mike   22  22000    500  110.0
2   2   Bob   12    550     12    5.5
3   3  Tone   32   6000     80   60.0
と表示される
"""

