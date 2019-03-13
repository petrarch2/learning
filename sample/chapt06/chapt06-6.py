import pandas
a = pandas.read_csv( 'sample.csv' )
print( a.loc[0] )
"""
id          0
name     Jone
age        18
value    1000
price      20
Name: 0, dtype: object
と表示される
"""
print( a.ix[1] )
"""
id           1
name      Mike
age         22
value    22000
price      500
Name: 1, dtype: object
と表示される
"""
b = a[a.id==3]
c = a[a.name=='Tone']
d = a[a.age==32]
print(b)
print(c)
print(d)
"""
   id  name  age  value  price
3   3  Tone   32   6000     80
と表示される
"""
e = b[['name','age']]
e.to_csv( 'sample2.csv' )
"""
,name,age
3,Tone,32
という中身のファイルが作成される
"""
f = pandas.read_csv( 'sample2.csv' )
print( f )
"""
   Unnamed: 0  name  age
0           3  Tone   32
と表示される
"""
g = pandas.read_csv( 'sample2.csv', header=0, index_col=0 )
print( g )
"""
   name  age
3  Tone   32
と表示される
"""
e.to_csv( 'sample3.csv', header=False, index=False )
"""
Tone,32
という中身のファイルが作成される
"""
