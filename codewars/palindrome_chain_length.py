__author__ = 'Tamby Kaghdo'

def palindrome_chain_length(num):
    steps = 0
    ispalindrome = False
    while ispalindrome == False:
        num_list = list(str(num))
        reversed_list = num_list[::-1]
        ispalindrome_lst = []
        for idx, val in enumerate(num_list):
            if (num_list[idx] == reversed_list[idx]):
                ispalindrome_lst.append(True)

            else:
                ispalindrome_lst.append(False)
        if all(ispalindrome_lst):
            ispalindrome = True
        else:
            ispalindrome = False
        num = num + int(''.join(reversed_list))
        steps += 1
    return steps-1


print(palindrome_chain_length(89))
print(palindrome_chain_length(4884))
#print(palindrome_chain_length(1234))
#print(palindrome_chain_length(8872688))
