# Grasshopper - Summation
# Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.
#
# For example:
# summation(2) -> 3
# 1 + 2

def summation(num):
    my_sum = 0
    while num >= 0:
        my_sum = my_sum + num
        num = num - 1
    return my_sum
    
