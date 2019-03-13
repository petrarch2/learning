class SayHello:
	target = 'you'
	def __init__( self, say ):
		self.say = say
	def setTarget( self, target ):
		self.target = target
	def printHello( self ):
		m = self.say + ', ' + self.target
		print( m )

b = SayHello( 'Hello' )

b.printHello()    # Hello, you　と表示される

b.setTarget( 'World' )
c = SayHello( 'How are you' )
c.setTarget( 'System' )

b.printHello()    # Hello, World　と表示される
c.printHello()    # How are you, System　と表示される

print( SayHello.target )    # you　と表示される
