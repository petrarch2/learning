import json
with open( 'sample.json', 'r' ) as f:
	data = json.loads( f.read() )    # dataにJSONデータが入る
print( data[ 0 ] )    # Hello!　と表示される
print( data[ 1 ] )    # {'language': 'Python'}　と表示される
print( data[ 1 ][ 'language' ] )    # Python 　と表示される
print( data[ 2 ][ 'greets' ][ 'target' ][ 0 ] )    # World 　と表示される
print( data[ 2 ][ 'greets' ][ 'target' ][ 1 ] )    # System 　と表示される
