def plusMinusVal( val1, val2 ):
	p = val1 + val2
	m = val1 - val2
	return p, m
a, b = plusMinusVal( 20, 10 )  # a=30, b=10となる
t = plusMinusVal( 20, 10 )
c = t[0]     # c=30となる
d = t[1]     # d=10となる
for s in plusMinusVal( 20, 10 ):
	print( s )
"""
30
10
と表示される
"""
