class Say:
	def printHello( self ):
		print( 'fmm...' )

class SayHello ( Say ):
	def __init__( self ):
		super( SayHello, self ).__init__()
		self.say = 'Hello'
		self.target = 'World'
	def printHello( self ):
		print( self.say + ', ' + self.target )

i = SayHello()
print( i.say )    # Hello　と表示される
print( i.target )    # World　と表示される
i.printHello()    # Hello, World　と表示される
