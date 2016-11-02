__author__ = 'Tamby Kaghdo'

import sys
import csv

def main():
    input_data_file = sys.argv[1]
    data_types_file = sys.argv[2]
    output_file = sys.argv[3]
    header = 'VARIABLE, LEVEL, Y, N, %Y, %N'
    factor_names_column_index = 0
    column_data_type_column_index = 1

    outfile = open(output_file, 'ab' )
    writer  = csv.writer(outfile)

    factor_lst = get_factor_list(data_types_file,factor_names_column_index,column_data_type_column_index)
    for factor_row, factor_value in enumerate(factor_lst):
        analyzed_column = factor_row
        variable_1 = factor_value
        if factor_value == 'ST_CODE':
            variable_2 = 'OWN_HOME'
        else:
            variable_2 = variable_1
        get_pivot_table(input_data_file, analyzed_column, header, variable_1,variable_2, writer)
        writer.writerow(" ")

    outfile.close()
    #end of main
def get_factor_list(file_name,factor_names_column_index,column_data_type_column_index):
    f = open(file_name, 'r')
    csvf = csv.reader(f)
    factor_lst = []
    for line in csvf:
        if line != '\n':
            if line[column_data_type_column_index].strip() == 'FACTOR':
                factor_lst.append(line[factor_names_column_index])
    # end for loop
    return factor_lst

def get_pivot_table(file_name, column, header,variable_1,variable_2,writer):
    # create a unique list of the factor
    unique_lst = get_unique_list(file_name, column)
    input_file_dict = put_file_in_dict(file_name)

    writer.writerow(["pivot table for the {0} and {1}:".format(variable_1,variable_2)])
    writer.writerow ([header])
    for lst_index, lst_value in enumerate(unique_lst):
        i = 0
        yes_counter = 0
        no_counter = 0
        sum = 0
        yes_percent = 0
        no_percent = 0
        for dict_index, dict_value in enumerate(input_file_dict):
            if lst_value == dict_value[variable_1] and dict_value[variable_2] == 'Y':
                yes_counter += 1
            elif lst_value == dict_value[variable_1] and dict_value[variable_2] == 'N':
                no_counter += 1
            sum += 1
            i += 1
        # end for loop
        yes_percent = (float(yes_counter) / float(sum)) * 100
        no_percent = (float(no_counter) / float(sum)) * 100
        pivot_row = '{0}, {1}, {2}, {3}, {4}, {5}'.format(variable_1, lst_value, yes_counter, no_counter, yes_percent, no_percent)
        writer.writerow([pivot_row])
        # end for loop


def put_file_in_dict(file_name):
    info = []
    with open(file_name, 'r') as csvfile:
        # read the CSV file into a dictionary
        dictReader = csv.DictReader(csvfile)
        for row in dictReader:
            info.append(row)
    return info


def get_unique_list(file_name, column_index):
    f = open(file_name, 'r')
    csvf = csv.reader(f)
    state_list = []
    unique_state_list = []

    # create a unique state list
    i = 0
    for line in csvf:
        if line != '\n' and i != 0:
            state_list.append(line[column_index])
        i += 1
    # end for loop

    unique_state_list = list(set(state_list))
    unique_state_list.sort()

    return unique_state_list
    # end get_unique_list


def print_list(lst):
    for l in lst:
        print l


if __name__ == '__main__':
    main()
