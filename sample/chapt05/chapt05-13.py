from bs4 import BeautifulSoup

# HTMLコードを準備
html = '''
<!DOCTYPE html>
<html>
<head>
<title>BeautifulSoup test</title>
</head>
<body>
<h1 id="hello">Hello, BeautifulSoup !</h1>
<h1 id="nice">Nice to meet you, HTTP !</h1>
<h1 id="how">How are you, HTML !</h1>
This is document.
</body>
</html>
'''

soup = BeautifulSoup( html )    # BeautifulSoupオブジェクトを作成
a = soup.title
print( a )    # <title>BeautifulSoup test</title>　と表示される
b = soup.h1
print( b )    # <h1 id="bigtext">Hello, BeautifulSoup !</h1>　と表示される
c = soup.h1[ 'id' ]
print( c )    # hello　と表示される
d = soup.h1.get( 'id' )
print( d )    # hello　と表示される
e = soup.h1.get( 'name' )
print( e )    # None　と表示される
f = soup.title.name    # title　と表示される
print( f )
g = soup.title.string    # BeautifulSoup test　と表示される
print( g )
h = soup.title.parent
print( h )
"""
<head>
<title>BeautifulSoup test</title>
</head>
と表示される
"""
i = soup.find_all( 'h1' )
print( len( i ) )    # 3　と表示される
print( i[0] )    # <h1 id="hello">Hello, BeautifulSoup !</h1>　と表示される
print( i[1].string )    # Nice to meet you, HTTP !　と表示される
print( i[2].name )    # h1　と表示される
j = soup.find( 'body' ).find( 'h1' )
print( j )    # <h1 id="hello">Hello, BeautifulSoup !</h1>　と表示される
k = soup.find( 'h1', id='nice' )
print( k )    # <h1 id="nice">Nice to meet you, HTTP !</h1>　と表示される
l = soup.select( 'body > h1#how' )
print( l )    # [<h1 id="how">How are you, HTML !</h1>]　と表示される
soup.find( 'h1', id='how' ).string = 'Fine!'
m = soup.select( 'body > h1#how' )
print( m )    # p[<h1 id="how">Fine!</h1>]　と表示される
