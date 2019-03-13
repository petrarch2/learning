from my_pack_b import *
import my_pack_b
a = dir(my_pack_b)
print( a )    # ['__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'file_b', 'file_c']　と表示される
