import re
q = 'Good morning, Jupyter Notebook'
r = re.match( 'Good', q )    #「Good」とマッチしたmatchクラスを返す
print( r.span() )    # マッチした場所：(0, 4)　と表示される
s = re.search( 'bo+k', q )    #「book」とマッチしたmatchクラスを返す
print( s.span() )    # マッチした場所：(26, 30)　と表示される
t = re.compile( 'bo+k' )    # 予め正規表現をコンパイルしておく
u = re.search( t, q )    #「book」とマッチしたmatchクラスを返す
print( u.span() )    # マッチした場所：(26, 30)　と表示される
v = 'whoo, Good morning, Jupyter Notebook, Yahoo!'
w = re.findall( '[A-Z][a-z]*', v )
print( w )    # ['Good', 'Jupyter', 'Notebook', 'Yahoo']　と表示される
x = re.findall( '[A-Z][a-z]*o{2}[a-z]*', v )
print( x )    # ['Good', 'Notebook', 'Yahoo']　と表示される
y = re.finditer( '[A-Z][a-z]*o{2}[a-z]*', v )
for z in y:
	print( z.span() )
"""
(6, 10)
(28, 36)
(38, 43)
と表示される
"""
