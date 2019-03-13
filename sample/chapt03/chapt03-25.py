class Say:
	def printHello( self, msg ):
		print( msg )

class SayHello ( Say ):
	def __init__( self ):
		super( SayHello, self ).__init__()
		self.say = 'Hello'
		self.target = 'World'
	def printHello( self, msg ):
		super().printHello( self.say + ', ' + self.target + msg )

j = SayHello()
print( j.say )    # Hello　と表示される
print( j.target )    # World　と表示される
j.printHello( ' and Python' )    # Hello, World and Python　と表示される
