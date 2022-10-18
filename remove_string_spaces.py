# Simple, remove the spaces from the string, then return the resultant string.
# 
# Python 3.10, kyu 8

def no_space(x):
    y = ''          # empty vector
    for i in x:     # iterate
        if i == ' ':    # if you find a space...
            print("I've found a space")   # personal control :)
            continue
        else:         # if you don't find a space...     
            y = y+i   # ...concatenate
    return y
  
# my test    
no_space("asd asd asd")
