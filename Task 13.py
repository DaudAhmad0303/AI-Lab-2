def input_binary():
    '''
    Python program which accepts a sequence of comma separated binary numbers as its input; 
    it checks for all the numbers whether they are binary or not,
    if the input numbers include other than binary numbers; it will ignore those ones
    i.e., string, symbols, decimal numbers. 
    
    It returns the list of binary numbers only
    '''
    lst = input('Enter 4 digit binary Numbers: ').split(',')
    lst_digits = []
    for i in range(len(lst)):
        if lst[i].isdigit() == True:
            # for j in lst[i]:
            try:
                lst_digits.append(int(lst[i], 2))
            except:
                pass
    return lst_digits

####        Driver Program      ####
bin_list = input_binary()
print('Binary Numbers multiple of 5 : ',end='')
for i in range(len(bin_list)):
    if bin_list[i] % 5 == 0:
        print(bin(bin_list[i]).replace('0b', ''), end=' ')