from datetime import date
l = date.today()
m = date( 2018, 12, 2 )
n = m.strftime( '%m/%d/%y. %d %b %Y is a %A' )
print( n )    # 12/02/18. 02 Dec 2018 is a Sunday　と表示される
from datetime import time
o = time( hour=14, minute=2, second=38 )
p = m.strftime( '%X is %H-%M-%S. it is %I%p' )
print( p )    # 14:02:38 is 14-02-38. it is 02PM　と表示される
from datetime import datetime
q = datetime.today()
r = datetime.now()
s = datetime( 2018, 12, 2, 14, 2, 38 )
t = s.strftime( '%m/%d/%y %H:%M:%S' )
print( t )    # 12/02/18 14:02:38　と表示される
from datetime import timezone
u = s.replace( tzinfo=timezone.utc )
v = u.strftime( '%m/%d/%y %H:%M:%S %z %Z' )
print( v )    # 12/02/18 14:02:38 +0000 UTC　と表示される
from datetime import timedelta
w = u.replace( tzinfo=timezone( timedelta( hours=+9 ) ) )    # タイムゾーンの更新だけ
x = w.strftime( '%m/%d/%y %H:%M:%S %z %Z' )
print( x )    # 12/02/18 14:02:38 +0900 UTC+09:00　と表示される

y = u.astimezone( timezone( timedelta( hours=+9 ) ) )    # タイムゾーンを更新して時刻を変更
z = y.strftime( '%m/%d/%y %H:%M:%S %z %Z' )
print( z )    # 12/02/18 23:02:38 +0900 UTC+09:00　と表示される
