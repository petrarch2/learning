class SayHello:
	pass
a = SayHello()
a.say = 'Hello'
a.target = 'World'
print( a.say )    # Hello　と表示される
print( a.target )    # World　と表示される
b = SayHello()
b.say = 'How are you'
b.target = 'System'
print( a.say + ', ' + b.target )    # Hello, System　と表示される
print( b.say + ', ' + a.target )    # How are you, World　と表示される
