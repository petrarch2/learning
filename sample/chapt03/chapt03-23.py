class Say:
	def printHello( self, msg ):
		print( msg )

class SayHello ( Say ):
	def __init__( self ):
		super( SayHello, self ).__init__()
		self.say = 'Hello'
		self.target = 'World'

h = SayHello()
print( h.say )    # Hello　と表示される
print( h.target )    # World　と表示される
h.printHello( h.say + ', ' + h.target )    # Hello, World　と表示される
