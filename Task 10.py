def FizzBuzz(s = 0, e = 51):
    '''
    Python program which iterates the integers from 1 to 50 by default if value is not specified.
    For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". 
    For numbers which are multiples of both three and five print "FizzBuzz".
    
    Sample Output :
    ```
        fizzbuzz
        1
        2
        fizz
        4
        buzz
    ```
    '''
    for i in range(s, e):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

####        Driver Program      ####
FizzBuzz()