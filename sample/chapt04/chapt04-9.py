import pandas
import numpy
a = pandas.DataFrame( [ [ 0, 'Jone', 18, 1000, 20],
	 [ 1, 'Mike', 22, 22000, 500],
	[ 2, 'Bob', 12, 550, 12],
	[ 3, 'Tone', 32, 6000, 80] ], columns=[
	'id', 'name', 'age', 'value', 'price' ] )
print( a )
"""
   id  name  age  value  price
0   0  Jone   18   1000     20
1   1  Mike   22  22000    500
2   2   Bob   12    550     12
3   3  Tone   32   6000     80
と表示される
"""
b = numpy.mean( a[ 'age' ] )    # age列の平均を計算
print( b )    # 21.0　と表示される
c = numpy.sum( a.ix[ 1, [ 'age', 'value', 'price' ] ] )    # 2行目のage,value,priceの合計を計算
print( c )    # 22522　と表示される

