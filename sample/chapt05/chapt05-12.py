from urllib import request
from xml.etree import ElementTree

zipcode = '1638001'
url = 'http://zip.cgis.biz/xml/zip.php?zn=%s' % zipcode

with request.urlopen( url ) as response:
	text = response.read().decode( 'utf-8' )
	data = ElementTree.fromstring( text )
d = {}
for val in data.find( 'ADDRESS_value' ):
	for keys in val.attrib.keys():
		d[ keys ] = val.attrib[ keys ]
print( d[ 'state' ] )    # 東京都　と表示される
print( d[ 'address' ] )    # 西新宿２丁目８−１　と表示される
print( d[ 'company' ] )    # 東京都庁　と表示される
