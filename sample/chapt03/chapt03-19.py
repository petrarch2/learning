class SayHello:
	def printHello( self ):
		print( self.say + ', ' + self.target )

c = SayHello()
c.say = 'Hello'
c.target = 'World'
c.printHello()    # Hello, World　と表示される
