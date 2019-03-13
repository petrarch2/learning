class SayHello:
	def __init__( self, say ):
		self.say = say
		self.target = []
	def setTarget( self, target ):
		self.target.append( target )
	def printHello( self ):
		m = self.say + ', ' + self.target[ -1 ]
		print( m )

f = SayHello( 'Hello' )
f.setTarget( 'World' )
g = SayHello( 'How are you' )
g.setTarget( 'System' )

f.printHello()    # Hello, World　と表示される
g.printHello()    # How are you, System　と表示される
