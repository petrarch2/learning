a = open( 'testfile.txt', 'r' )    # ファイルを読み込みモードで開く
a.close()    # 開いたファイルを閉じる
b = b'Hello, World!'    # bはASCIIの「Hello, World!」が入ったバイト列
print( b )    # b'Hello, World!'　と表示される
c = bytes.fromhex( '00 12 24 48 8F' )
print( c.hex() )    # 001224488f　と表示される
d = bytes( 5 )
print( d.hex() )    # 0000000000　と表示される
e = [ 0x00, 0x12, 0x24, 0x48, 0x8F ]
f = bytes( e )
print( f.hex() )    # 001224488f　と表示される
g = open( 'testfile.txt', 'r' )
h = g.read( 10 )    # testfile.txtから10バイト読み込む（hは文字列型）
i = g.readline()    # testfile.txtから一行読み込む（iは文字列型）
g.close()
j = open( 'testfile.bin', 'rb' )
k = j.read( 10 )    # testfile.binから10バイト読み込む（kはバイト列型）
j.close()
l = open( 'testfile.txt', 'r' )
m = l.readlines()    # testfile.txtから全ての行を読み込む
l.close()
n = open( 'testfile.txt', 'r' )
o = list( n )    # testfile.txtの全ての行をリストにする
n.close()
p = open( 'testfile.txt', 'w' )
p.write( 'Hello, World!' )    # ファイルに文字列型を書き込む
p.close()
q = open( 'testfile.bin', 'wb' )
q.write( bytes.fromhex( '00 12 24 48 8F' ) )    # ファイルにバイト列型を書き込む
q.close()
r = open( 'testfile.bin', 'wb+' )
r.write( bytes.fromhex( '00 12 24 48 8F' ) )    # ファイルにバイト列型を書き込む
r.seek( 0 )    # ファイルの先頭に移動
s = r.read( 1 )    # 1バイト読み込む
print( s.hex() )    # 00　と表示される
r.seek( 3 )    # 3バイト目に移動
t = r.read( 1 )    # 1バイト読み込む
print( t.hex() )    # 48　と表示される
r.seek( -3, 2 )    # 後ろから3バイト目に移動
u = r.read( 1 )    # 1バイト読み込む
print( u.hex() )    # 24　と表示される
r.close()
with open( 'testfile.bin', 'wb+' ) as v:
	v.write( bytes.fromhex( '00 12 24 48 8F' ) )
# ファイルが自動で閉じられる
