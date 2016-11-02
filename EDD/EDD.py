#!/usr/bin/python

import sys
import os
import csv
import operator



def create_var_dict( data_type_file ):
    # initialize variable dictionary and open data type file
    var_dict = {}
    f = open(data_type_file, 'r' )
    csvf = csv.reader(f)

    # loop over each line and load variable, data_type into var_dict
    for line in csvf:
        if line != '\n':
            var_dict[ line[0] ] = line[1].strip()

    return var_dict


def process_numeric( variable_file ):
    # initialize variables
    count    = 0
    unfilled = 0
    filled   = 0
    the_sum  = 0
    the_min  = 999999999.    # just shy of 1 billion
    the_max  = -999999999.   # just shy of -1 billion

    with open( variable_file ) as row:
        next(row)   # skip header row

        # actions to do for each record
        for number in row:
            count += 1
            if number == '' or number == '\n':  # check to see if no data is present
                unfilled += 1
            else:                               # data present --> process
                filled += 1
                number = float(number)
                the_sum = the_sum + number
                # update min and max
                if number < the_min:
                    the_min = number
                if number > the_max:
                    the_max = number

    # sanity check: determine whether # filled + # unfilled = count
    if filled + unfilled != count:
        sys.exit("There is an error: # filled + # unfilled does not equal the count!")

    # calculations
    fill_rate = round( 100 * ( float(filled) / count ), 1)
    mean = round( float(the_sum) / filled, 1)

    # print outputs
    print "Filled: %d"       % filled
    print "Unfilled: %d"     % unfilled
    print "Count: %d"        % count
    print "Fill rate: %0.1f" % fill_rate
    print "Sum: %d"          % the_sum
    print "Mean: %0.1f"      % mean
    print "Min: %d"          % the_min
    print "Max: %d"          % the_max

    return count, filled, unfilled, fill_rate, the_sum, mean, the_min, the_max


def process_factor( variable_file ):
    # initialize variables
    keys = {}
    count    = 0
    unfilled = 0
    filled   = 0

    with open( variable_file ) as row:
        next(row)   # skip header row

        # actions to do for each record
        for factor in row:
            count += 1
            factor = factor.strip()         # removes whitespace and \n
            if factor == '':                # check to see if no data is present
                unfilled += 1
            else:                           # data present --> process
                filled += 1
                if factor in keys:
                    keys[factor] += 1
                else:
                    keys[factor] = 1

    # sanity check: determine whether # filled + # unfilled = count
    if filled + unfilled != count:
        sys.exit("There is an error: # filled + # unfilled does not equal the count (# records)!")

    # calculations
    fill_rate = round( 100 * ( float(filled) / count ), 1)

    factors     = keys.keys()
    num_factors = len(factors)

    # determine top 10 factors
    sorted_factors = sorted( keys.items(), key=operator.itemgetter(1), reverse=True )
    if len(sorted_factors) >= 10:
        top_factors_temp = sorted_factors[:10]
    else:
        top_factors_temp = sorted_factors
    # format top factors list
    top_factors = []
    for kv in top_factors_temp:
        the_factor = kv[0]
        the_freq   = kv[1]
        the_frac  = 100 * ( float(the_freq) / filled )
        final_form = '%s : %d : %0.1f' % ( the_factor, the_freq, the_frac )
        top_factors.append( final_form )

    # print outputs
    print "Count: %d"                    % count
    print "Filled: %d"                   % filled
    print "Unfilled: %d"                 % unfilled
    print "Fill rate: %0.1f"             % fill_rate
    print "Number of unique factors: %d" % num_factors
    print "Top 10 unique factors: %s"    % top_factors

    return count, filled, unfilled, fill_rate, num_factors, top_factors


def main():
    args = sys.argv[1:]

    in_data_types_file  = args[0]       # variable_name, data_type
    column_file         = args[1]       # file with variable name and associated column
    # out_data_types_file = args[2]       # blank file

    var_dict = create_var_dict( in_data_types_file )

    # process column according to data type
    f = open( column_file )
    contents = f.readlines()
    header = contents[0].strip()
    var_data_type = var_dict[header]

    print "This column is of type: %s" % ( var_data_type )


    #########################################################################################################
    ## Process variable according to data type, add characterization to FINAL output file
    #########################################################################################################

    infile  = open( in_data_types_file, 'r' )
    outfile = open( 'data_types_FINAL.csv', 'ab' )
    reader  = csv.reader( infile )
    writer  = csv.writer( outfile )


    ###############################
    ## NUMERIC
    ###############################
    if var_data_type == 'NUMERIC':
        count, filled, unfilled, fill_rate, the_sum, mean, the_min, the_max = process_numeric( column_file )

        # write variable characterization to file
        for line in reader:
            var_name    = line[0]
            data_type   = line[1]
            num_factors = ''        # not defined for numeric columns
            top_factors = ''        # not defined for numeric columns
            if var_name == header:
                new_row = [var_name, data_type, count, filled, unfilled, fill_rate,
                           the_min, the_max, the_sum, mean, num_factors, top_factors]
                writer.writerow( new_row )
        infile.close()
        outfile.close()

    ###############################
    ## FACTOR
    ###############################
    if var_data_type == 'FACTOR' or var_data_type == 'DATE' or var_data_type == 'STRING':
        count, filled, unfilled, fill_rate, num_factors, top_factors = process_factor( column_file )

        # write variable characterization to file
        for line in reader:
            var_name  = line[0]
            data_type = line[1]
            the_min = ''            # not defined for factor columns
            the_max = ''            # not defined for factor columns
            the_sum = ''            # not defined for factor columns
            mean = ''               # not defined for factor columns
            if var_name == header:
                new_row = [var_name, data_type, count, filled, unfilled, fill_rate,
                           the_min, the_max, the_sum, mean, num_factors, top_factors]
                writer.writerow( new_row )
        infile.close()
        outfile.close()


    f.close()


if __name__ == '__main__':
    main()

