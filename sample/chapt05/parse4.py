class ParseError( Exception ):
	pass

class HelloParser:
	def __init__( self, filename ):
		self.filename = filename
		self.stack = []
		
	def get_indent( self ):
		return '  ' * len(self.stack)
		
	def read_one( self, file ):
		line = file.readline()
		if not line:
			return None
		elif line[0] == '>':
			starttag = line[1:].strip()
			xmltag = self.get_indent() + '<%s>'%starttag
			self.stack.append( starttag )
			return xmltag
		elif line[0] == '<':
			endtag = self.stack.pop()
			return self.get_indent() + '</%s>'%endtag
		elif line[0] == ':':
			leaf = line[1:].strip()
			return self.get_indent() + '<p>%s</p>'%leaf
		else:
			raise ParseError
	
	def read_file( self ):
		with open( self.filename ) as file:
			tag = self.read_one( file )
			while tag:
				yield tag
				tag = self.read_one( file )
	
	def __iter__( self ):
		return self.read_file()

try:
	for tag in HelloParser( 'mk.txt' ):
		print(tag)
except ParseError:
	print('Parse Error!')
finally:
	pass
	