# You're at the zoo... all the meerkats look weird. Something has gone terribly wrong - someone has gone and switched their heads and tails around!
# 
# Save the animals by switching them back. You will be given an array which will have three values (tail, body, head). It is your job to re-arrange the array so that the animal is the right way round (head, body, tail).
# 
# Same goes for all the other arrays/lists that you will get in the tests: you have to change the element positions with the same exact logics
# 
# Simples!
# Python 3.10, kyu 8
# Note: instructions are confusing, it looks like you only need to exchange the first and last element (0 --> 2 and 2 --> 0)


def fix_the_meerkat(arr):
    fixed_arr = [' '] * int(len(arr))     # create an empty array, its size is equal to len(arr)
    fixed_arr[0] = arr[2]                 # accessing arr element by its index
    fixed_arr[1] = arr[1]
    fixed_arr[2] = arr[0]
    # print("input: ", arr)               # line 17 and line 18: just to check the array/s 
    # print("fixed array: ", fixed_arr)
    return fixed_arr
