import sys

def collatz(number):
    if False == isinstance(number,int) :     #判断类型
        print('Error:Invalid argument.')
        sys.exit()

    if 0 == number%2:
        number = number/2
    else:
        number = 3*number+1

    print(int(number))
    return number


value=int(input('input value for int:'))

while 1 != value:
    value = int(collatz(value))
print('Program End.')