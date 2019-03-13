import threading
# import dummy_threading  as threading    # threadingが使用できない場合

a = [ 1, 2, 3 ]

import threading
import random
import time

class MyThread( threading.Thread ):
	def run( self ):
		time.sleep( random.random() )
		print( 'Thread', a )

b = MyThread()

b.start()

time.sleep( random.random() )
a[ 0 ] = 4
print( 'Main', a )

b.join()

a[ 2 ] = 6
print( 'Finish', a )
