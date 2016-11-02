__author__ = 'Tamby Kaghdo'

def maskify(s):
    lst_s = list(s)
    masked_part = lst_s[0:-4]
    unmasked_part = lst_s[len(masked_part):len(lst_s)]
    masked_part = ["#" for i in masked_part]
    return ''.join(masked_part) + ''.join(unmasked_part)

str = "123456789"
print(maskify(str))

