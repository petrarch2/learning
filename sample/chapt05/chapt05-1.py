a = 'Hello'
b = "World"
c = 'Hello \
World'
d = '''
Hello,
World
'''
print( a )    # Hello　と表示される
print( b )    # World　と表示される
print( c )    # Hello World　と表示される
print( d )
"""

Hello,
World

と表示される
"""
e = 'say, \"Hello, World\"'
f = r'row string -> \ is not escaped'
g = '\N{smile}  \N{ghost}  \N{grinning face}'
print( e )    # say, "Hello, World"　と表示される
print( f )    # row string -> \ is not escaped　と表示される
print( g )    # ⌣  👻  😀　と表示される
h = 'How are you, System'
print( h[ 2 ] )    # w　と表示される
print( h[ 7:11 ] )    # you　と表示される
print( h[ 13: ] )    # System　と表示される
i = 'Hello'
j = 'World'
k = i + ', ' + j    # k = Hello, World　となる
k += ' and System'    # k = Hello, World and System　となる
