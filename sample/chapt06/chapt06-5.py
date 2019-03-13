import pickle
class MyData:
	def __init__( self, text ):
		self.text = text
	def printText( self ):
		print( self.text )

a = MyData( 'Hello, World' )
b = MyData( 'How are you, System' )
c = MyData( 'Nice to meet you, Python' )

with open( 'sample.pickle', 'wb' ) as f:
	pickle.dump( [ a, b, c ], f, pickle.HIGHEST_PROTOCOL )

with open( 'sample.pickle', 'rb' ) as f:
	data = pickle.load( f )

data[0].printText()    # Hello, World　と表示される
data[1].printText()    # How are you, System　と表示される
data[2].printText()    # Nice to meet you, Python　と表示される
