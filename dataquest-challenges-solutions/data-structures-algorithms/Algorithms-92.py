## 2. Implementing an algorithm ##

# When Kobe is found in the dataset, store his position in Kobe_position
kobe_position = ""

# Find Kobe in the dataset
for i in nba:
    if i[0] == "Kobe Bryant":
        kobe_position = i[1]


## 4. Linear search revisited ##

# player_age returns the age of a player in our nba dataset
def player_age(name):
    age = None
    for i in nba:
        if i[0] == name:
            age = i[2]
            break
    if age != None:
        return age
    else:
        return -1
    
allen_age = player_age("Ray Allen")
durant_age = player_age("Kevin Durant")
shaq_age = player_age("Shaquille O'Neal")

## 7. Example constant time algorithms ##

# Implementation A: Convert degrees Celcius to degrees Fahrenheit
def celcius_to_fahrenheit(degrees):
    step_1 = degrees * 1.8
    step_2 = step_1 + 32
    return step_2

# Implementation B: Reverse a list
def reverse(ls):
    length = len(ls)
    new_list = []
    for i in range(length):
        new_list[i] = ls[length - i]
    return new_list

# Implementation C: Print a blastoff message after a countdown
def blastoff(message):
    count = 10
    for i in range(count):
        print(count - i)
    print(message)

not_constant = "B"

## 10. Some other algorithms ##

# Find the length of a list
def length(ls):
    count = 0
    for elem in ls:
        count = count + 1
length_time_complexity = "linear"

# Check if a list is empty -- Implementation 1
def is_empty_1(ls):
    if length(ls) == 0:
        return True
    else:
        return False
is_empty_1_complexity = "linear"

# Check if a list is empty -- Implementation 2
def is_empty_2(ls):
    for element in ls:
        return False
    return True
is_empty_2_complexity = "constant"