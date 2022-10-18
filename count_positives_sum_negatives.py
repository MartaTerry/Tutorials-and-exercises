# Given an array of integers.
# 
# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.
# 
# If the input is an empty array or is null, return an empty array.
# 
# Python 3.10, kyu 8

# version 1: Error: [0, 0] should equal []
def count_positives_sum_negatives(arr):
    count_positive = 0
    sum_negative = 0
    
    for number in arr:
        if int(number) > 0:
            count_positive = count_positive + 1
        elif int(number) < 0:
            sum_negative = sum_negative - number
        else:
            continue
    return [count_positive, -sum_negative]

    if None in arr:
        return []

# my test
print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
print(count_positives_sum_negatives([0,0,0,0,0,0,0,0,0]),[0,0])
print(count_positives_sum_negatives([]),[])


# version 2: Error: [0, 0] should equal []
def count_positives_sum_negatives2(arr):
    count_positive = 0
    sum_negative = 0

    for number in arr:
        if int(number) > 0:
            count_positive = count_positive + 1
        elif int(number) < 0:
            sum_negative = sum_negative - number
        elif int(number) == 0:
            continue
        else:
            empty_arr = []
            return empty_arr
    return [count_positive, -sum_negative]


print(count_positives_sum_negatives2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
print(count_positives_sum_negatives2([0,0,0,0,0,0,0,0,0]),[0,0])
print(count_positives_sum_negatives2([]),[])
