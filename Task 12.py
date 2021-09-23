def input_multi_lines():
    '''
    Python program that accepts a sequence of lines (blank line to terminate) as
    input and return that string.
    '''
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    return '\n'.join(lines)

####        Driver Program      ####
print(input_multi_lines().lower())
