__author__ = 'Tamby Kaghdo'

#My solution to Multiples of 3 and 5 Kata from codewars.com
def solution(number):
    lst = list(range(1,number))
    sum = 0
    for i in lst:
        if (i % 3 == 0) or (i % 5 == 0):
            sum += i
    return sum

def main():
    print(solution(10))

if __name__ == '__main__':
    main()
