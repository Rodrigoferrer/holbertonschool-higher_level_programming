#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # iterate and store smaller lists into i
    if matrix == [[]]:
            print()
    for i in matrix:
        # iterate over list in i storing each value
        # into j
        for j in i:
            # condition for when end is not reached
            if j != i[-1]:
                print("{:d}".format(j), end=" ")
            # condition for when end IS reached
            else:
                # when printing without end arg, end is a line break by
                # default
                print("{:d}".format(j))        