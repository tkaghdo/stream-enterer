## 3. Base cases ##

# Recursive factorial function
def factorial(n):
    # Check the base case
    if n == 0:
        return 1
    # Recursive case
    return n * factorial(n - 1)

factorial1 = factorial(1)
factorial5 = factorial(5)
factorial25 = factorial(25)

## 5. Fibonacci ##

# Add your function below
def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n-1) + fib(n-2)

fib1 = fib(1)
fib5 = fib(5)
fib25 = fib(25)
    

## 7. Linked List Length ##

# First person's name
first_item = people.head().get_data()

# Getting linked list length using iteration
def length_iterative(ls):
    count = 0
    while not ls.is_empty():
        count = count + 1
        ls = ls.tail()
    return count

def length_recursive(ls):
    if ls.is_empty():
        return 0
    return 1 + length_recursive(ls.tail())
people_length = length_recursive(people)

## 9. Linked List Time Complexity ##

# Retrieving an item in the linked list by index
retrieval_by_index = "linear"

# Retrieving an item in the linked list by value
retrieval_by_value = "linear"

# Deleting an item from the linked list, with access to the item and 
#     the item before it
deletion = "constant"

# Inserting an item into the linked list, with access to the location
#     where we are inserting
insertion = "constant"

# Calculating the length of a linked list using a loop
length_iterative = "linear"

# Calculating the length of a linked list using recursion
length_recursive = "linear"