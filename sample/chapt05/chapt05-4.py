a = 'Hello, World'
b = a.startswith( 'Hello' )    # Helloで始まっているか
print( b )    # True　と表示される
c = a.endswith( 'World' )    # Worldで終わっているか
print( c )    # True　と表示される
d = ( a[ 0:5 ] == 'Hello' )    # 0から5文字の場所がHelloか
print( d )    # True　と表示される
e = 'How are you, System'
f = e.find( 'you' )    # youの登場する位置を取得
print( f )    # 8　と表示される
g = e.index( 'you' )    # youの登場する位置を取得
print( g )    # 8　と表示される
h = 'you' in e    # youが含まれるか
print( h )    # True　と表示される
i = e.count( 'o' )    # oの出現する回数を数える
print( i )    # 2　と表示される
j = e.count( 'o', 0, 4 )    # oの出現する回数を、0から3文字の場所から数える
print( j )    # 1　と表示される
k = 'Good morning, Jupyter Notebook'
l = k.replace( 'morning', 'night' )
print( l )    # Good night, Jupyter Notebook　と表示される
m = k.replace( 'o', '0' )    # oを全て0に置換
print( m )    # G00d m0rning, Jupyter N0teb00k　と表示される
n = k.replace( 'o', '0', 2 )    # oを最初の2個だけ0に置換
print( n )    # G00d morning, Jupyter Notebook　と表示される
o = '0'.join( k.split( 'o' ) )    # oで区切った後0で結合
print( o )    # G00d m0rning, Jupyter N0teb00k　と表示される
p = '0'.join( k.split( 'o' ) [ 3:6 ] )    # oで区切った後範囲を指定して0で結合
print( p )    # rning, Jupyter N0teb0　と表示される
