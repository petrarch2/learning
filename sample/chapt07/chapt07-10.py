import threading
import time

g = threading.Lock()    # ロックを作成

def h():    # 並列処理の内容
	with g:
		# 排他的に行いたい処理
		for j in range( 5 ):
			print( 'Hello' )
			time.sleep( 1 )
	return

i = threading.Thread( target=h )

i.start()    # 並列処理を開始

with g:
	# 排他的に行いたい処理
	for j in range( 5 ):
		print( 'World' )
		time.sleep( 1 )

i.join()    # 並列処理を終了
