# In this simple assignment you are given a number and have to make it negative. 
# But maybe the number is already negative?
# Python 3.10, kyu 8

def make_negative( number ):
    if number > 0:
        print('is greater than zero')
        return int(-number)
    elif number < 0:
        print('is lower than zero')
        return number
    else:
        return number
# my test:    
make_negative(0)
make_negative(2)
make_negative(-2)
