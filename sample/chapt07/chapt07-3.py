import os
import sys
j = os.getcwd()    # カレントディレクトリを取得
print( j )    # 現在のカレントディレクトリが表示される
os.chdir( '/' )    # カレントディレクトリを変更
k = os.getcwd()
print( k )    # /　と表示される
os.mkdir( 'hello' )
os.makedirs( 'nice/to/meet/you' )
os.remove( 'test' )
os.rmdir( 'hello' )
os.removedirs( 'nice/to/meet/you' )
