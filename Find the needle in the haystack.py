# Can you find the needle in the haystack?
# 
# Write a function findNeedle() that takes an array full of junk but containing one "needle"
# 
# After your function finds the needle it should return a message (as a string) that says:
# 
# "found the needle at position " plus the index it found the needle
# Python 3.10, kyu 8

def find_needle(haystack):
    for element in haystack:        # iterate through the array
        if element == "needle":     
            position = haystack.index(element)    # determine needle position
            message = 'found the needle at position ' + str(position)   # create the message
            return(message)

# my test
find_needle([1, 2, 3, "needle", 5])   # expected output: found the needle at position 3
