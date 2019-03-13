from xml.etree import ElementTree
file = ElementTree.parse( 'sample.xml' )    # XMLファイルを読み込む
filedata = file.getroot()    # XMLファイル内のルートエレメントを取得
data = ElementTree.fromstring( '''
<root id="main">
say
<data1 id="first">Hello</data1>
<data2 id="second">World</data2>
</root>''' )    # XML文字列内のエレメントを取得
print( data.tag )    # root　と表示される
print( data.attrib )    # {'id': 'main'}　と表示される
print( data.attrib[ 'id' ] )    # main　と表示される
print( data.text )
"""

say

と表示される
"""
for c in data:
	print( c.attrib[ 'id' ] + ' -> ' + c.text )
"""
first -> Hello
second -> World
と表示される
"""
