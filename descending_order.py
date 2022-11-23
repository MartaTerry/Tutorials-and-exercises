# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.
# Examples:
# Input: 42145 Output: 54421
# 
# Input: 145263 Output: 654321
# 
# Input: 123456789 Output: 987654321
# 
# Python 3.10, kyu 7

def descending_order(num):
    my_numbers = []
    for n in str(num):
        my_numbers.extend(n)
        
    my_numbers.sort(reverse = True)
    join_numbers = ("").join(my_numbers)
    join_numbers.replace(" ","")
    final = int(join_numbers)
    return final
