def fahr_to_cel( F = 0):
    '''
    Convert temperatures to Fahrenheit from Celsius.
    '''
    return (F - 32) * (5 / 9)

def cel_to_fahr( C = 0):
    '''
    Convert temperatures from Celsius to Fahrenheit.
    '''
    return (9 / 5) * C + 32 

####        Driver Program     ####
# Conversion
# C = (F - 32) * (5 / 9)
# F = (9 / 5 ) * C + 32
degree_sign = u"\N{DEGREE SIGN}"
Temp = float(input("Enter Temperature in Celsius: "))
print("{}{}C is {:.2f} in Fahrenheit".format(Temp, degree_sign, fahr_to_cel(Temp)))

Temp = float(input("Enter Temperature in Fahrenheit: "))
print("{}{}C is {:.2f} in Celsius".format(Temp, degree_sign, cel_to_fahr(Temp)))

