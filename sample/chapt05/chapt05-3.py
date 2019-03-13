l = [ 'Nice', 'to', 'meet', 'you', 'Python' ]
m = ' '.join( l )    # 空白文字を区切りに使用して繋げる
print( m )    # Nice to meet you Python　と表示される
n = ','.join( l )    # カンマを区切りに使用して繋げる
print( n )    # Nice,to,meet,you,Python　と表示される
o = ' \n  How are you, Pyton ?? \n'
p = o.strip()    # 前後のホワイトスペースを削除
print( p )    # How are you, Pyton ??　と表示される
q = p.lower()    # 小文字に変換
print( q )    # how are you, pyton ??　と表示される
r = p.upper()    # 大文字に変換
print( r )    # HOW ARE YOU, PYTON ??　と表示される
s = p.swapcase()    # 小文字と大文字を入れ替える
print( s )    # hOW ARE YOU, pYTON ??　と表示される
t = p.title()    # 単語の頭文字が大文字になるように変換する
print( t )    # How Are You, Pyton ??　と表示される
u = p.split( ' ' )    # 空白で区切ってリストにする
print( u )    # ['How', 'are', 'you,', 'Pyton', '??']　と表示される
v = o.splitlines()    # 改行で区切ってリストにする
print( v )    # [' ', '  How are you, Pyton ?? ']　と表示される
u = p.partition( ',' )    # 最初に登場する「,」とその前後を取得する
print( u )    # ('How are you', ',', ' Pyton ??')　と表示される
v = p.isalpha()    # アルファベットのみか
print( v )    # Falseと表示される
w = p.isalnum()    # アルファベットと数字のみか
print( w )    # Falseと表示される
# x = p.isascii()    # ASCII文字列かどうか（Python3.7以降）
# print( x )    # Trueと表示される
y = p.isdigit()    # 数字のみか
print( y )    # Falseと表示される
z = p.isspace()    # ホワイトスペースのみか
print( z )    # Falseと表示される
