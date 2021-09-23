def is_even(num):
    '''
    Check wether the number is even odd and return True if it's Even
    >>> print(is_even(4))
        True
    '''
    return num % 2 == 0

def input_list():
    '''
    Inputs a series of numbers also checks for string literals and ignore them
    from Input in list and returns a list of digits
    '''
    lst = list(input("Enter a series: "))
    lst1 = []
    for i in range(len(lst)):
        if lst[i].isdigit() == True:
            lst1.append(int(lst[i]))
    return lst1

####    Driver Program      ####
series = input_list()
even = 0
odd = 0
for i in series:
    if is_even(i) == True:
        even += 1
    else:
        odd += 1
print(f'Number of Even digits: {even}\nNumber of Odd digits: {odd}')