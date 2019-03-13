import os
import sys
a = os.name
print( a )    # posix 又は nt　と表示される
b = sys.platform
print( b )    # OSの種類が表示される
c = os.uname()    # Unix交換OSのみ
print( c.sysname )    # Linux　等のOSの名前
print( c.nodename )    # ip-172-31-8-41　等のネットワーク上の名
print( c.release )    # 4.4.0-1069-aws　等のOSのバージョン
print( c.version )    # ＃79-Ubuntu SMP Mon Sep 24　等の詳細なバージョン
print( c.machine )    # x86_64　等のCPUの名前
d = os.getlogin()
print( d )    # OSのログインユーザー名が表示される
e = os.get_terminal_size()
print( e[0], e[1] )    # コンソールのサイズが表示される
f = os.getpid()
print( f )    # 実行中のプロセスIDが表示される
g = os.getppid()
print( g )    # 親プロセスのプロセスIDが表示される
h = os.getenv( 'HOME' )
os.putenv( 'PATH', '/' )
os.unsetenv( 'LD_PATH' )
i = os.environ[ 'HOME' ]
os.environ[ 'PATH' ] = '/'
del os.environ[ 'LD_PATH' ]
