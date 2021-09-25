def print_range(s = 1500, e = 2701):
    '''
    Finds those numbers which are divisible by 7 and multiple of 
    5, between 1500 and 2700 (both included)
    '''
    for i in range(1500, 2701):
        if i % 7 == 0 and i % 5 == 0:
            print(i , end=" ")

####        Driver Program     ####
print_range()