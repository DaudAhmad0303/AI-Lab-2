def reverse_str1(string = 'civic'):
    '''
    Accepts a word from the user and reverse it.
    '''
    reversed_str = ''
    # reversed_str = ''.join(reversed(string))
    for i in string:
        reversed_str = i + reversed_str
    return reversed_str

def reverse_str2(string = 'civic'):
    '''
    Accepts a word from the user and reverse it.
    '''
    return string[::-1]

print(reverse_str1("Daud"))
print(reverse_str2("Daud"))