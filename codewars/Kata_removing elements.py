__author__ = 'Tamby Kaghdo'

#My solution to Removing Elements Kata from codewars.com
def remove_every_other(my_list):
    every_other_list = []
    counter = 0
    for i in my_list:
        if counter % 2 == 0 :
            every_other_list.append(i)
        counter += 1
    return every_other_list

def main():

    my_list = ['Keep', 'Remove', 'Keep', 'Remove', 'Keep']
    print(remove_every_other(my_list))

    my_list = ['Hello', 'Goodbye', 'Hello Again']
    print(remove_every_other(my_list))

    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(remove_every_other(my_list))

    my_list = [[1, 2]]
    print(remove_every_other(my_list))

    my_list = [['Goodbye'], {'Great': 'Job'}]
    print(remove_every_other(my_list))

if __name__ == '__main__':
    main()

