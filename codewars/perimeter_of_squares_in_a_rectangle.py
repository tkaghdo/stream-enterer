__author__ = 'Tamby Kaghdo'


def fib(n, computed = {0: 0, 1: 1}):
     if n not in computed:
         computed[n] = fib(n-1, computed) + fib(n-2, computed)
     return computed[n]

def perimeter(n):
    sum = 0
    for i in range(n+1):
        sum += fib(i+1)
    return 4 * sum


print(perimeter(400))


#perimeter(5)  #should return 80
#perimeter(7)  #should return 216
