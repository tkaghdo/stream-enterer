__author__ = 'Tamby Kaghdo'
from operator import add
from functools import reduce
def f(num):
    if isinstance(num, int ) and num > 0:
        s = reduce(add, range(1,num+1))
        return s
    else:
        return None

#print(f(100))
