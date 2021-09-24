def password_validator():
    '''
    Python program to check the validity of password input by users, and returns True or False
    Validation :
    1. At least 1 letter between [a-z] and 1 letter between [A-Z].
    2. At least 1 number between [0-9].
    3. At least 1 character from [$#@].
    4. Minimum length 6 characters.
    5. Maximum length 16 characters.
    '''
    string = input('Input your Password: ')
    count_num = 0
    count_sym = 0
    count_ALPH = 0
    count_alph = 0
    symbols = ['!','@','#','$','%',"'",',','"','[',']','{','}',';',':',',','.',',','?','&','^','*','(',')','-']
    val = 0
    if len(string) > 16 or len(string) < 6:
        return False
    for i in range(len(string)):
        if string[i].isdigit():
            count_num += 1
        if string[i].islower():
            count_alph += 1
        if string[i].isupper():
            count_ALPH += 1
        if string[i] in symbols:
            count_sym += 1
    if count_alph == 0 or count_ALPH == 0 or count_num == 0 or count_sym == 0:
        return False
    else: 
        return True

####        Driver Program      ####
val = password_validator()
if val:
    print('Password is Valid...')
else:
    print('Password is not Valid...')
