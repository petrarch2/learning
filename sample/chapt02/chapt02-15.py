a = 0
while True:
	a = a + 1
	if a < 10:
		continue
	print( a )    # 「10」と表示される
	break
print( 'loop ended' )    # 「loop ended」と表示される
