import json
data = ['Hello!', 
		{'language': 'Python'}, 
		{'greets': {'target': ['World', 'System']}}
	]
with open( 'sample.json', 'w' ) as f:
	f.write( json.dumps( data ) )
