__author__ = 'Tamby Kaghdo'

#My solution to the Kata: Excel's COUNTIF, SUMIF and AVERAGEIF functions

def to_num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

def count_if(values,criteria):
    ops = [">","<","<=",">=","<>"]
    counter = 0
    condition_part = ""
    value_part = None
    if type(criteria) is str:
        if len(criteria) >= 3 and (criteria[1] == "=" or criteria[1] == ">"):
            condition_part = criteria[0] + criteria[1]
            value_part = to_num(criteria[2:])
        elif criteria[0] in ops:
            condition_part = criteria[0]
            value_part = to_num(criteria[1:])
        elif criteria not in ops:
			for i in values:
				if i == criteria:
					counter += 1

        if condition_part == ">=":
            for i in values:
                if i >= value_part:
                    counter += 1
        elif condition_part == "<=":
            for i in values:
                if i <= value_part:
                    counter += 1
        elif condition_part == "<>":
            for i in values:
                if i != value_part:
                    counter += 1
        elif condition_part == ">":
            for i in values:
                if i > value_part:
                    counter += 1
        elif condition_part == "<":
            for i in values:
                if i < value_part:
                    counter += 1
    elif type(criteria) is int or type(criteria) is float:
        for i in values:
            if i == criteria:
                counter += 1

    return counter

def sum_if(values,criteria):
    sum = 0

    if type(criteria) is str:
        if criteria[1] == "=" or criteria[1] == ">":
            condition_part = criteria[0] + criteria[1]
            value_part = to_num(criteria[2:])
        else:
            condition_part = criteria[0]
            value_part = to_num(criteria[1:])

        if condition_part == ">=":
            for i in values:
                if i >= value_part:
                    sum += i
        elif condition_part == "<=":
            for i in values:
                if i <= value_part:
                    sum += i
        elif condition_part == ">":
            for i in values:
                if i > value_part:
                    sum += i
        elif condition_part == "<":
            for i in values:
                if i < value_part:
                    sum += i
        elif condition_part == "<>":
            for i in values:
                if i != value_part:
                    sum += i

    elif type(criteria) is int or type(criteria) is float:
        for i in values:
            if i == criteria:
              sum += i

    return sum

def average_if(values,criteria):
    sum = sum_if(values,criteria)
    num = 0
    if type(criteria) is str:
        if criteria[1] == "=" or criteria[1] == ">":
            condition_part = criteria[0] + criteria[1]
            value_part = to_num(criteria[2:])
        else:
            condition_part = criteria[0]
            value_part = to_num(criteria[1:])

        if condition_part == ">=":
            for i in values:
                if i >= value_part:
                    num += 1
        if condition_part == "<=":
            for i in values:
                if i <= value_part:
                    num += 1
        if condition_part == ">":
            for i in values:
                if i > value_part:
                    num += 1
        if condition_part == "<":
            for i in values:
                if i < value_part:
                    num += 1
        if condition_part == "<>":
            for i in values:
                if i <> value_part:
                    num += 1

    elif type(criteria) is int or type(criteria) is float:
        for i in values:
            if i == criteria:
              num += 1

    return float(sum) / float(num)

def main():
    print(sum_if([1,3,5,3,0,-1,-5],'<>1'))
    pass


if __name__ == '__main__':
    main()

