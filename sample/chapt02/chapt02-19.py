def showMsg( msg1, msg2='Good morning', msg3='See you later' ):
	print( msg1 )
	print( msg2 )
	print( msg3 )
# 最初と二つ目の引数を指定する
showMsg( 'Hello, World', msg2='How are you, System' )
"""
Hello, World
How are you, System
See you later
と表示される
"""

# 最初と三つ目の引数を指定する
showMsg( 'Hello, World', msg3='Nice to meet you, Python' )
"""
Hello, World
Good morning
Nice to meet you, Python
と表示される
"""

# 最初と三つ目の引数を指定する
showMsg( msg1='Hello, World', msg3='Nice to meet you, Python' )
"""
Hello, World
Good morning
Nice to meet you, Python
と表示される
"""

# 三つの引数を順不同に指定する
showMsg( msg1='Hello, World', msg3='Nice to meet you, Python', msg2='How are you, System' )
"""
Hello, World
How are you, System
Nice to meet you, Python
と表示される
"""
