__author__ = 'Tamby Kaghdo'

def next_bigger(num):
    str_lst = list(str(num))
    end_lst = int(''.join(sorted(list(str(num)), reverse=True)))
    if num == end_lst:
        return -1
    else:
        i = len(str_lst)-1
        save_loc_1 = -9
        largest_to_left = None
        while i >= 0:
            if str_lst[i-1] < str_lst[i]:
                largest_to_left = int(str_lst[i-1])
                save_loc_1 = i - 1
                break
            i -= 1
        sub_lst = str_lst[save_loc_1+1:len(str_lst)]
        right_side = [int(x) for x in sub_lst]
        next_largest_right_side = 999
        right_side_index = -9
        for i, v in enumerate(right_side):
            if v - largest_to_left > 0 and v - largest_to_left < next_largest_right_side:
                next_largest_right_side = v
                right_side_index = i

        temp_right_side = str_lst[save_loc_1:len(str_lst)]

        temp_left_side = str_lst[:save_loc_1]
        temp_left_side = temp_left_side + list(str_lst[save_loc_1 + right_side_index + 1])
        del temp_right_side[right_side_index+1]
        lst_before_sort = temp_left_side + temp_right_side
        final__str_lst = lst_before_sort[0:len(temp_left_side)] + sorted(lst_before_sort[len(temp_left_side):])
        final_int_lst = [int(x) for x in final__str_lst]
        next_largest_num = int(''.join(map(str,final_int_lst)))
        return next_largest_num



    #print(str_lst[save_loc_1])

print(next_bigger(123456784987654321))
print(next_bigger(12))
print(next_bigger(513))#==531
print(next_bigger(2017))#==2071
print(next_bigger(9))#==-1
print(next_bigger(111))#==-1
print(next_bigger(531))#==-1
print(next_bigger(414))
print(next_bigger(84585839394958583929292929948502029394858))

