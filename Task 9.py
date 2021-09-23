def print_fibonacci_series(s = 0, e = 50):
    '''
    Python program to get the Fibonacci series between 0 to 50 by default if no range is given.
    If provided then return list for the given range.
    
    Note : The Fibonacci Sequence is the series of numbers :
    0, 1, 1, 2, 3, 5, 8, 13, 21, ....

    '''
    lst = [1, 1]
    count = 50 
    temp = 1
    for i in range(1, 50):
        lst.append(lst[i] + lst[i-1])
    return lst

####       Driver Program       ####
print_fibonacci_series()