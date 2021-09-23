def print_pattern(num = 9):
    '''
    Python program to construct the following pattern, using a nested for loop:
    *
    * *
    * * *
    * * * *
    * * * * *
    * * * *
    * * *
    * *
    *
    Mayukai Alucard
    Mayukai Mirage
    Mayukai Mono
    Mayukai Reversal
    One Dark Pro
    
    '''
    num = num // 2 + 1
    for i in range(num):
        for j in range(i):
            print("*", end=" ")
        print()
    for i in range(num, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()

length = int(input("Enter a number above 3: "))
print(f'Required Pattern of length {length} is as follows:')
print_pattern(length)