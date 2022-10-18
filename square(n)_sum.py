# Complete the square sum function so that it squares each number passed into it and then sums the results together.
# 
# For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.
# Python 3.10, kyu 8

def square_sum(numbers):
    y = 0     # "initialize" an integer
    for number in numbers:
        # print('original number: ' + str(number))    # print "original number"
        number = (number)**2 
        # print('new number: ' + str(number))         # print "square number"
        y = y + number     # sum of n square numbers
    return y

# my test
square_sum([1, 2, 2])
