__author__ = 'Tamby Kaghdo'

from random import randint
import random

#My solution to Don't Rely on Luck Kata from codewars.com
random.seed(1)
lucky_number = randint(1,100)
print(lucky_number)

#in this case the guess was 14. it doesn't change because I set the seed
