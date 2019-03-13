import pickle
data = ['Hello!', 
		{'language': 'Python'}, 
		{'greets': {'target': ['World', 'System']}}
	]
with open( 'sample.pickle', 'wb' ) as f:
	pickle.dump( data, f, pickle.HIGHEST_PROTOCOL )
