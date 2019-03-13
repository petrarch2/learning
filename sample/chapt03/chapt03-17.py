import pandas
df = pandas.DataFrame( 
	{ 'Name_1': [1, 2, 3], 'Name_2': [12.34, 34.56, 56.78] },
	index=[ 'A', 'B', 'C' ] )
print( df )
#    Name_1  Name_2
# A       1   12.34
# B       2   34.56
# C       3   56.78
# と表示される
df = pandas.DataFrame( [ [1, 12.34], [2, 34.56], [3, 56.78] ] )
print( df )
#    0      1
# 0  1  12.34
# 1  2  34.56
# 2  3  56.78
# と表示される
df.columns = [ 'Name_1', 'Name_2' ]
print( df )
#   Name_1  Name_2
# 0       1   12.34
# 1       2   34.56
# 2       3   56.78
# と表示される
df.index=[ 'A', 'B', 'C' ]
print( df )
#    Name_1  Name_2
# A       1   12.34
# B       2   34.56
# C       3   56.78
# と表示される
al = df [ 'Name_1' ]    # 1列目のデータだけを取り出す
print( al )
# A    1
# B    2
# C    3
# Name: Name_1, dtype: int64
# と表示される
am = al[ 'A' ]
print( am )    # 1　と表示される
an = df.loc[ 'A' ]
ao = df.iloc[ 0 ]
ap = df.ix[ 'A' ]
aq = df.ix[ 0 ]   # 1行目のデータだけを取り出す
print( aq )
# Name_1     1.00
# Name_2    12.34
# Name: A, dtype: float64
# と表示される
ar = aq[ 'Name_1' ]
print( ar )    # 1.0　と表示される
ar = df.loc[ 'A', 'Name_1' ]
at = df.iloc[ 0, 0 ]
au = df.ix[ 'A', 'Name_1' ]
av = df.ix[ 0, 'Name_1' ]
print( av )    # 1.0　と表示される
aw = df.ix[ [ 'A', 'B' ], 'Name_1' ]
ax = df.ix[ [ 0, 1 ], 'Name_1' ]
print( ax )
# A    1
# B    2
# Name: Name_1, dtype: int64
# と表示される
ay = df.values
print( ay )
# [[ 1.   12.34]
# [ 2.   34.56]
# [ 3.   56.78]]
# と表示される(ayはndarray型)
az = ay.tolist()
print( az )    # [[1.0, 12.34], [2.0, 34.56], [3.0, 56.78]]　と表示される(azはリスト)
