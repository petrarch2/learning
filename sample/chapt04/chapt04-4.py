a = 'Hello, World'
b = 'How are you, System'
a = None    # aという変数自体は残る
del b    # bという変数自体を削除
print( a )    # Noneと表示される
# print( b )    # 変数bが存在しないためエラー
import gc
gc.disable()     # 一時的にガベージコレクションを停止
c = "Hello, World"    # cをメモリ上に展開
del c    # cを削除
gc.collect()    # cが使用していたメモリを解法
gc.enable()     # ガベージコレクションを再開
