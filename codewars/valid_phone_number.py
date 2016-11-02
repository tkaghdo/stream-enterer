__author__ = 'Tamby Kaghdo'
import re
def validPhoneNumber(num):
    if re.match("\([0-9]{3}\) [0-9]{3}-{1}[0-9]{4}$",num):
        return True
    else:
        return False

print(validPhoneNumber("(123) 456-7890"))  #=>  returns true
print(validPhoneNumber("(1111)555 2345"))  #=> returns false
print(validPhoneNumber("(098) 123 4567"))  #=> returns false
print(validPhoneNumber("(1a3) 456-7890"))
print(validPhoneNumber("(123) 456-7fg0"))
print(validPhoneNumber("(12c) 4th6-7890"))
print(validPhoneNumber("(a23) 456-7890"))
print(validPhoneNumber("asdfad(123) 456-78904adsfs"))
print(validPhoneNumber("(123) 456-7890abc)"))

