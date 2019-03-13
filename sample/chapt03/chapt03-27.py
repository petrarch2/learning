class Howareyou:
	def printHello( self ):
		print( 'How are you' )

class Nicetomeetoyou:
	def printHello( self, target ):
		print( 'Nice to meet you, ' + target )

class Say ( Howareyou, Nicetomeetoyou ):
	pass

l = Howareyou()
l.printHello()    # How are you　と表示される

m = Nicetomeetoyou()
m.printHello( 'Python' )    # Nice to meet you, Python　と表示される

n = Say()
n.printHello()    # How are you　と表示される
# n.printHello( 'Python' )    # エラーとなる
