def print_fibonacci_series():
    '''
    Python program to get the Fibonacci series between 0 to 50.
    
    Note : The Fibonacci Sequence is the series of numbers :
    0, 1, 1, 2, 3, 5, 8, 13, 21, ....

    '''
    lst = [1, 1]
    count = 50 
    temp = 1
    for i in range(1, 50):
        lst.append(lst[i] + lst[i-1])
    for item in lst:    print(item)

####       Driver Program       ####
print_fibonacci_series()