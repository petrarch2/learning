class SayHello:
	target = []
	def __init__( self, say ):
		self.say = say
	def setTarget( self, target ):
		self.target.append( target )
	def printHello( self ):
		m = self.say + ', ' + self.target[ -1 ]
		print( m )

d = SayHello( 'Hello' )
d.setTarget( 'World' )
e = SayHello( 'How are you' )
e.setTarget( 'System' )

d.printHello()    # Hello, System　と表示される　←注意！
e.printHello()    # How are you, System　と表示される
