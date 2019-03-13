m = 'Hello, World'
m = 'How are you, System'
print( m )    # 「How are you, System」と表示される

m = 'Hello, World'
for m in 'ABC':
	print( m )
	
print( m )   # 「C」と表示される

m = 'Hello, World'
a = [ m for m in 'ABC' ]
print( m )    # 「Hello, World」と表示される


