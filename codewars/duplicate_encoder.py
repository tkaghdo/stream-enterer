__author__ = 'Tamby Kaghdo'

def encoder(str):
    lst = [x.lower() for x in list(str)]
    d_lst = []
    for i in lst:
        count = 0
        for j in lst:
            if i == j:
                count += 1
        if count == 1:
            d_lst.append("(")
        else:
            d_lst.append(")")
    return ''.join(d_lst)
print(encoder("din"))# => "((("
print(encoder("recede")) #=> "()()()"
print(encoder("Success")) #=> ")())())"
print(encoder("(( @")) #=> "))(("
