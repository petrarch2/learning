m = 'Hello, World'
def printHello():
	global m
	m = 'How are you, System'
	print( m )

printHello()    # 「How are you, System」と表示される
print( m )    # 「How are you, System」と表示される
