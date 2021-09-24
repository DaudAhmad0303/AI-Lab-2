####        Driver Program      ####
string = input("Enter your string: ")
letter = 0
digit = 0
for i in string:
    if i.isdigit() == True:
        digit += 1
    if i.isalpha() == True:
        letter += 1
print(f'Letters: {letter}\nDigits: {digit}')