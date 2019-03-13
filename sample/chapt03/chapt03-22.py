class SayHello:
	def __init__( self, say, hello ):
		self.say = say
		self.target = hello
	def printHello( self ):
		print( self.say + ', ' + self.target )

g = SayHello( 'Hello', 'World' )
print( g.say )    # Hello　と表示される
print( g.target )    # World　と表示される
g.printHello()    # Hello, World　と表示される
