def print_2d_array(rows = 0, column = 0):
    '''
    Python program which takes two digits m (row) and n (column) as input and
    generates a two-dimensional array. The element value in the i-th row and j-th column of
    the array should be i*j.
    >>> print_2d_array(3, 4)
    [
        [0, 0, 0, 0],
        [0, 1, 2, 3],
        [0, 2, 4, 6]
    ]
    '''
    # Declaring list of the specified size
    lst = [[0 for i in range(column)] for j in range(rows)]
    for i in range(rows):
        for j in range(column):
            lst[i][j] = i*j
    
    # Printing the 2-D Array/List
    for i in lst:
        for j in i:
            print(j, end = ' ')
        print()

####        Driver Program      ####
rows = int(input('No. of Rows: '))
column = int(input('No. of Columns: '))
print_2d_array(rows, column)