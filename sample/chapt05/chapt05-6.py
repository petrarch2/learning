a = 'World'
b = f'Hello, {a}'    # b = 'Hello, World'　となる
c = 100
d = 20
e = f'sum of CandD = {c+d}'    # e = 'sum of CandD = 120'　となる
f = f'max of CandD = {max(c,d)}'    # e = 'max of CandD = 100'　となる
g = 'Hello, {0}'
h = g.format( 'World' )    # h = 'Hello, World'　となる
i = '{say} are you, {target}'
j = i.format( say='How', target='System' )    # j = 'How are you, System'　となる
k = '{0[0]} to meet you, {0[1]}'
l = ( 'Nice', 'Python' )
m = k.format( l )    # m = 'Nice to meet you, Python'　となる
n = 'Hello'
o = '{:<10}'.format( n )    # o = 'Hello     '　となる
p = '{:>10}'.format( n )    # p = '     Hello'　となる
q = '{:^10}'.format( n )    # q = '  Hello   '　となる
r = '{:*^10}'.format( n )    # r = '**Hello***'　となる
s = 'World'
t = 'Hello, %s' % s    # t = 'Hello, World'　となる
u = 100
v = 'pine'
w = '%d pieces of %s' % (u, v)    # w = '100 pieces of pine'　となる
x = 'Hello'
y = 'World'
z = '%(say)s, %(target)s' % { 'say': x, 'target': y }    # z = 'Hello, World'　となる
