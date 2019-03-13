import os
import sys
os.system( '/bin/echo Hello World!' )    # Hello World!　と表示される
os.execv( '/bin/echo', [ 'echo', 'Hello', 'World!' ] )    # Hello World!　と表示して終了
