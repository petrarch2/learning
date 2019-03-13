a = 10    # 整数として認識される
b = 10.0    # 浮動小数点として認識される
print( a )   # 10 と表示される
print( b )   # 10.0 と表示される
c = int( 10 )    # 整数値としてaに10を代入
d = float( 10 )    # 浮動小数点値としてbに10を代入
e = complex( 10 )    # 複素数値としてcに10を代入
print( c )   # 10 と表示される
print( d )   # 10.0 と表示される
print( e )   # (10+0j) と表示される 
print( c == d )    # Trueと表示される
print( c == e )    # Trueと表示される
print( hash( d ) == hash( e ) )    # Trueと表示される
print( hash( d ) == hash( c ) )    # Trueと表示される
import sys
print( sys.float_info )
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1) と表示される
print( sys.float_info.min )
# 2.2250738585072014e-308 と表示される
print( sys.float_info.max )
# 1.7976931348623157e+308 と表示される
f = complex( 10, 2 )
g = complex( 10, 4 )
print( f )  # (10+2j) と表示される
print( g )  # (10+4j) と表示される
print( c + f )  # (20+2j) と表示される
print( f + g )  # (20+6j) と表示される
