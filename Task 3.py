from random import randint
def guess_num(num):
    '''
    Program to guess a number between 1 to 9.
    '''
    if num == randint(0, 9):
        return True
    else:
        return False

####        Driver Program     ####
while True:
    val = int(input("Guess a number between 0, 9: "))
    if guess_num(val) == True:
        print('Well guessed!')
        break
    else:
        guess_num(val)