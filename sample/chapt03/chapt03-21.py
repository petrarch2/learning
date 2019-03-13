class SayHello:
	say = 'Hello'    # 使用しない方が良い
	target = 'World'    # 使用しない方が良い
	def printHello( self ):
		print( self.say + ', ' + self.target )

f = SayHello()
print( f.say )    # Hello　と表示される
print( f.target )    # World　と表示される
f.printHello()    # Hello, World　と表示される
