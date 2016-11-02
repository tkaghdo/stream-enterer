__author__ = 'Tamby Kaghdo'
"""
Regex Validate Pin Code
https://www.codewars.com/kata/regex-validate-pin-code
"""

import re
import sys

def validate_pin(code):
    """
    A function that return True if the pin code is in the correct format.

    :param code: a string that represents a pin code
    format "####", ex."1234" or "######", ex. #123456"
    :return: a boolean; True if valid. Else return False
    """
    if re.match("^\d{4}(?:\d{2})?$",code):
        return True
    else:
        return False

def main():
    '''
    Main function of the program
    '''

    status = True
    from optparse import OptionParser

    use = '''Usage: %prog pin_code
    pin_code: a numeric pin code with 4 or 6 digits
    '''
    parser = OptionParser(usage=use)
    (options, args) = parser.parse_args()
    if len(args) != 1:
        parser.error("incorrect number of arguments")
        status = False
    else:
        print validate_pin(sys.argv[1])
    return status

if __name__ == "__main__":
    # call main
    sys.exit(0 if main() else 1)

