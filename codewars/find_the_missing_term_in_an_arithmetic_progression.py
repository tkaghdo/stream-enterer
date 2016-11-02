__author__ = 'Tamby Kaghdo'

def find_missing(incomplete_seq):
    first_number = incomplete_seq[0]
    last_number = incomplete_seq[len(incomplete_seq)-1]
    seq = (last_number - first_number)/len(incomplete_seq)
    missing_number = None
    for i, v in enumerate(incomplete_seq):
        if incomplete_seq[i+1] == incomplete_seq[i] + seq:
            pass
        else:
            missing_number = incomplete_seq[i] + seq
            break
    return missing_number

print(find_missing([1,3,5,9,11])) # => 7
print(find_missing([1, 2, 3, 4, 6, 7, 8, 9])) # 5
