class MyWith:
	def __init__( self, text ):
		self.text = text

	def __enter__( self ):
		print( 'enter - ' + self.text )
		return self

	def __exit__( self, exc_type, exc_value, traceback ):
		print( 'exit - ' + self.text )
		return True

with MyWith( 'Hello' ) as w:
	print( 'process - ' + w.text )
"""
enter - Hello
process - Hello
exit - Hello
と表示される
"""
