class MyIter:
	def __iter__( self ):
		self.a = 0
		return self
	def __next__( self ):
		self.a += 1
		if self.a == 10:
			raise StopIteration
		return self.a
b = MyIter()
for c in b:
	print( c )
"""
1
2
3
4
5
6
7
8
9
と表示される
"""