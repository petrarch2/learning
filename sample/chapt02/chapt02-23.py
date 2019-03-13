import time

def sleepthree( x ):
	time.sleep( 3 )
	return x

i = [ 1, 2, 3, 4 ]
start = time.time()    # 開始時間を取得
print( 'before map', time.time() - start )    # 経過時間を表示
j = map( sleepthree, i )
print( 'after map', time.time() - start )    # 経過時間を表示
for j in j:
	print( 'in loop', j, time.time() - start )    # 経過時間を表示
"""
before map 0.0008533000946044922
after map 0.0022416114807128906
in loop 1 3.0065736770629883
in loop 2 6.009757995605469
in loop 3 9.012943267822266
in loop 4 12.016127109527588
と表示される
"""
