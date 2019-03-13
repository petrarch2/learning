m = 'fmm...'
def printHello():
	m = 'Hi, you'
	def setHello():
		m = 'Hello, World'
	def setHowareyou():
		global m
		m = 'How are you, System'
	def setNicetomeetyou():
		nonlocal m
		m = 'Nice to meet you, Python'
	print( m )    # 1行目の出力
	setHello()
	print( m )    # 2行目の出力
	setHowareyou()
	print( m )    # 3行目の出力
	setNicetomeetyou()
	print( m )    # 4行目の出力

printHello()
print( m )    # 5行目の出力
