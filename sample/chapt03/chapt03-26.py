class Say:
	def printHello( self, msg ):
		print( msg )

class Hello:
	def __init__( self, say, target ):
		self.say = say
		self.target = target

class SayHello ( Say, Hello ):
	def __init__( self ):
		super( SayHello, self ).__init__( 'Hello', 'World' )
	def printHello( self, msg ):
		super().printHello( self.say + ', ' + self.target + msg )

k = SayHello()
print( k.say )    # Hello　と表示される
print( k.target )    # World　と表示される
k.printHello( ' and Python' )    # Hello, World and Python　と表示される
