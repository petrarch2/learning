import json
import numpy
a = json.dumps( [1,2,3] )    # a = '[1, 2, 3]'　となる
# b = json.dumps( numpy.array( [1, 2, 3] ) )    # エラーとなる
