def showMsg( msg1, msg2='Good morning', msg3='See you later' ):
	print( msg1 )
	print( msg2 )
	print( msg3 )
# 三つ引数を指定する
showMsg( 'Hello, World', 'How are you, System', 'Nice to meet you, Python' )
"""
Hello, World
How are you, System
Nice to meet you, Python
と表示される
"""

# 二つ引数を指定する（最後の引数はデフォルトの値）
showMsg( 'Hello, World', 'How are you, System' )
"""
Hello, World
How are you, System
See you later
と表示される
"""

# 一つ引数を指定する（残り二つの引数はデフォルトの値）
showMsg( 'Hello, World' )
"""
Hello, World
Good morning
See you later
と表示される
"""
