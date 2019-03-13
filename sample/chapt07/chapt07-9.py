d = [ 1, 2, 3 ]

import threading
import random
import time

class MyThreadFunction():
	def __call__( self ):
		time.sleep( random.random() )
		print( 'Thread', d )

e = MyThreadFunction()
f = threading.Thread( target=e )

f.start()

time.sleep( random.random() )
d[ 0 ] = 4
print( 'Main', d )

f.join()

d[ 2 ] = 6
print( 'Finish', d )
