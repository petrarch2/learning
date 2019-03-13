import multiprocessing
import random
import time

a = [ 1, 2, 3 ]
b = [ 'A', 'B' ]

def p( d ):
	time.sleep( random.random() )
	print( 'subProsess ' + d, a )
	if d == 'A':
		return 'Hello, World'
	elif d == 'B':
		return 'How are you, System'

c = multiprocessing.Pool( 2 )

a[ 0 ] = 4

print( 'mainProsess ', a )
# mainProsess  [4, 2, 3]　と表示される

f = c.map( p, b )
"""
subProsess B [1, 2, 3]
subProsess A [1, 2, 3]
と表示される
"""

for g in f:
	print( g )
"""
Hello, World
How are you, System
と表示される
"""
