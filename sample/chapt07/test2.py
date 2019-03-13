import argparse
parser = argparse.ArgumentParser( description='Argument Test' )
parser.add_argument( '--message', '-m', default='hello', help='Message String' )
parser.add_argument( '--num', '-n', type=int, default=1, help='Exclamation Num' )
parser.add_argument( '--flag', '-f', action='store_true', help='To Uppercase' )
args = parser.parse_args()

message = args.message
num = args.num
flag = args.flag
if flag:
	print( message.upper() + '!' * num )
else:
	print( message + '!' * num )
