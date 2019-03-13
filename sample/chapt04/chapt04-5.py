import gc
import weakref

class MemoryData:    # クラスを作成
	pass

d = MemoryData()    # クラスのインスタンスを作成
d.data = 'Hello, World'    # メモリ上にデータを作成
e = weakref.ref( d )    # 弱参照を作成
# del d    # 元の参照を削除 -- 注：ガベージコレクションが即時実行される環境だとeも削除される。
print( e().data )    # Hello, World　と表示される
gc.collect()    # ガベージコレクションを実行
print( e() )    # None　と表示される
