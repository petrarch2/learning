import pandas
import numpy
d = pandas.DataFrame( [ [ 0, 'Jone', 18, 1000, 20],
	 [ 1, 'Mike', 22, 22000, 500],
	[ 2, 'Bob', 12, 550, 12],
	[ 3, 'Tone', 32, 6000, 80] ], columns=[
	'id', 'name', 'age', 'value', 'price' ] )
print( d.mean() )    # 平均値を計算
"""
id          1.5
age        21.0
value    7387.5
price     153.0
dtype: float64
と表示される
"""
print( d.max() )    # 最大値を取得
"""
id           3
name      Tone
age         32
value    22000
price      500
dtype: object
と表示される
"""
print( d.min() )    # 最小値を取得
"""
id         0
name     Bob
age       12
value    550
price     12
dtype: object
と表示される
"""
print( d.var() )    # 分散を計算
"""
id       1.666667e+00
age      7.066667e+01
value    1.010006e+08
price    5.443600e+04
dtype: float64
と表示される
"""
print( d.std() )    # 標準偏差を計算
"""
id           1.290994
age          8.406347
value    10049.906716
price      233.315237
dtype: float64
と表示される
"""
e = pandas.DataFrame( [ [ 0, 'Jone', 18, 1000, 20],
	 [ 1, 'Mike', 22, 22000, 500],
	[ 2, 'Bob', 12, 550, 12],
	[ 3, 'Tone', 32, 6000, 80] ], columns=[
	'id', 'name', 'age', 'value', 'price' ] )
print( e.describe() )    # 統計情報を取得
"""
             id        age         value       price
count  4.000000   4.000000      4.000000    4.000000
mean   1.500000  21.000000   7387.500000  153.000000
std    1.290994   8.406347  10049.906716  233.315237
min    0.000000  12.000000    550.000000   12.000000
25%    0.750000  16.500000    887.500000   18.000000
50%    1.500000  20.000000   3500.000000   50.000000
75%    2.250000  24.500000  10000.000000  185.000000
max    3.000000  32.000000  22000.000000  500.000000
と表示される
"""
print( e.corr() )    # 相関係数を取得
"""
             id       age     value     price
id     1.000000  0.491436 -0.082856 -0.170424
age    0.491436  1.000000  0.315843  0.205983
value -0.082856  0.315843  1.000000  0.993043
price -0.170424  0.205983  0.993043  1.000000
と表示される
"""