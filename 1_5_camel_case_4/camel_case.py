# Enter your code here. Read input from STDIN. Print output to STDOUT

import fileinput  
import re 

"""
operations:
    S: split - lower case
    C: combine - space-delimited
    
    M: method - terminate with ()
    V: variable
    C: class - start with caps
    
""" 
for line in fileinput.input():
    single_ln = line.split('\n', 1)[0]
    
    ln_list = single_ln.split(';', 2)

    # if split
    if ln_list[0] == 'S':
        if ln_list[1] == 'M':
            ln_list[2] = re.sub("[()]", "", ln_list[2])

        out = re.findall('[a-zA-Z][^A-Z]*', ln_list[2])
        [print(_.lower(), end= " ") for _ in out[:-1]]
        print(out[-1].lower(), end= "")
        print('\r')
        
    # if combine
    elif ln_list[0] == 'C':
        ln_stripped = ln_list[2].split()
        # if class
        if ln_list[1] == 'C':            
            [print(_.capitalize(), end='') for _ in ln_stripped]
        # if variable
        elif ln_list[1] == 'V' or 'M':
            print(ln_stripped[0], end="")
            [print(_.capitalize(), end='') for _ in ln_stripped[1:]]
        # if method
        if ln_list[1] == 'M':
            print('()', end="")
        print('\r')
