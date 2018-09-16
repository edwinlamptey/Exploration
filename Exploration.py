import xlwings as xw
import numpy as np

@xw.func
def get_sum(param1, param2):
    return param1 + param2


@xw.func
def get_product(param1, param2):
    return param1 * param2


@xw.func
def get_array(param1, param2):
    return [param1, param2]

@xw.func
@xw.arg('x', np.array, ndim=1)
@xw.arg('y', np.array, ndim=1)
def get_array2(x,y):
#    return [[param1,param2], [param1*2,param2*2]]
    n = np.array([x*2,y*2])
    return n

@xw.func
@xw.arg('x', np.array, ndim=2)
def add_one(x):
    return x + 1

x = get_array2(4,5)
print(x)

