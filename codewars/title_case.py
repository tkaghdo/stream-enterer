__author__ = 'Tamby Kaghdo'
def title_case(title, minor_words=""):
    t_lst = title.split()
    m_lst = minor_words.split()
    n_m_lst = []
    for i in m_lst:
        n_m_lst.append(i.lower())
    n_lst = []
    counter = 0
    for i in t_lst:
        if (i.lower() not in n_m_lst or counter == 0) and minor_words != "":
            n_lst.append(i.capitalize())
        elif minor_words == "":
             n_lst.append(i.capitalize())
        else:
            n_lst.append(i.lower())
        counter += 1

    return ' '.join(n_lst)


print(title_case('a clash of KINGS', 'a an the of')) # should return: 'A Clash of Kings'
print(title_case('THE WIND IN THE WILLOWS', 'The In')) # should return: 'The Wind in the Willows'
print(title_case('the quick brown fox')) # should return: 'The Quick Brown Fox'