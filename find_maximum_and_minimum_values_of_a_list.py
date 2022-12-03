# Your task is to make two functions ( max and min, or maximum and minimum, etc., depending on the language ) that receive a list of integers as input, 
# and return the largest and lowest number in that list, respectively. Examples (Input -> Output)
#
# [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
#
# Python 3.10, kyu 8

def minimum(arr):
    my_numbers = arr[0]
    for number in arr:
        if number != my_numbers:
            if number < my_numbers:
                my_numbers = number
    return my_numbers

def maximum(arr):
    my_numbers = arr[0]
    for number in arr:
        if number != my_numbers:
            if number > my_numbers:
                my_numbers = number
    return my_numbers
