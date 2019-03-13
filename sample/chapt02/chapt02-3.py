with open( 'filename.txt', 'w' ) as f:
	pass
# これはコメントです
print( 'Hello, World' )
print( 'Hello, World' )  # これはコメントです
"""
with open( 'filename.txt', 'w' ) as f:
	f.write( 'Hello, World\n' )
# これは間違ったコメントです
	f.write( 'How are you, System\n' )
"""
with open( 'filename.txt', 'w' ) as f:
	f.write( 'Hello, World\n' )
	# これは正しいコメントです
	f.write( 'How are you, System\n' )
""" 複数の行をコメントにする

この文字列は慣習的にコメントとして扱われます
"""
print( 'Hello, World' )
