a = -10
b = -a     # b = -( -10 ) なのでbは10
c = b + -a - +10     # c = 10 + - ( -10 ) - 10 なのでcは10
d = 10 + 10    # 10足す10でdは20
e = 20 - 10    # 20引く10でeは10
f = 10 * 10    # 10かける10でfは100
g = 15 / 2    # 15割る2でgは7.5
h = 15 // 2    # 15割る2（小数点以下切り捨て）でhは7
i = 15 % 2    # 15割る2の余りでhは1
import numpy
j = numpy.array([1,2]) @ numpy.array([3,4])    # jは11となる
k = numpy.array([[1,2],[3,4]]) @ numpy.array([[3,4],[5,6]])    # kは[[13,16],[29,36]]となる
print( k )
"""
 [[13 16]
  [29 36]]    と表示される
"""
l = 10
l += 10    # lに10を足すのでlは20
l *= 2    # lに2をかけるのでlは40
l /= 10    # lを10で割るのでlは4.0 (割り算で浮動小数点になる)
m = 13    # mは2進数で1101
n = m << 1    # nは2進数で11010 = 十進数の26
o = m << 2    # oは2進数で110100 = 十進数の52
p = m >> 1    # pは2進数で110 = 十進数の6
q = 13    # qは2進数で1101
r = 7    # rは2進数で111
s = q & r    # sは2進数で101 = 10進数の5
t = q | r    # tは2進数で1111 = 10進数の15
u = q ^ r    # uは2進数で1010 = 10進数の10
