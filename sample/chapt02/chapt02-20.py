def plusVal( val1, val2 ):
	r = val1 + val2
	return r
a = 10 + 20    # a=30となる
b = plusVal( 10, 20 )    # b=30となる

c = 10 + 20 + 30    # c=60となる
d = plusVal( 10, 20 ) + 30    # d=60となる
e = 10 + plusVal( 20, 30 )    # e=60となる
