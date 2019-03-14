import sys

def collatz(number):
    if False == isinstance(number,int) :     #判断类型
        print('Error:Invalid argument.')
        sys.exit()

    if 0 == number%2:
        number = number//2
    else:
        number = 3*number+1

    print(int(number))
    return number

try:
    value = int(input('input value for int:'))
except ValueError:
    print('Please input Int Type.')         #这里能不能跳转回input
else:
    while 1 != value:
        value = collatz(value)
    #print('Program End.')