__author__ = 'Tamby Kaghdo'
import unittest as Test
import re
def to_cents(num):
    #print(num)
    found = re.search("^\$(\d+)\.(\d{2})\Z",num)
    if found == None:
        return None
    else:
        return int(found.group(1) + found.group(2))


#print(to_cents(""))
print(to_cents("1"))
print(to_cents("1.23"))
print(to_cents("$1"))
print(to_cents("$12345678.90"))
print(to_cents("$9.69"))
print(to_cents("$9.70"))
print(to_cents("$9.71"))
print(to_cents("$1.23\n"))
print(to_cents("\n$1.23"))
print(to_cents("$0.69"))
print(to_cents("$9.69$4.3.7"))
print(to_cents("$9.692"))


