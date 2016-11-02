__author__ = 'Tamby Kaghdo'

def anagrams(word,word_list):
    l = []
    i_lst = []
    f_lst = []
    sorted_word = ''.join(sorted(word))
    #print(sorted_word)
    for w in word_list:
        l.append(''.join(sorted(w)))

    for i, v in enumerate(l):
        if v == sorted_word:
             i_lst.append(i)
    #print(i_lst)
    for i in i_lst:
        for indx, val in enumerate(word_list):
            if i == indx:
                f_lst.append(val)
    return f_lst


anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) #=> ['aabb', 'bbaa']
anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) #=> ['carer', 'racer']
anagrams('laser', ['lazing', 'lazy',  'lacer']) #=> []