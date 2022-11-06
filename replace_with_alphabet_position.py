import string

def alphabet_position(text):
    alphabet = list(string.ascii_lowercase)     # alphabet string
    alpha_index = {}                            # empty dictionary
    count = 1                                   # counter
    
    for k in alphabet:
        alpha_index[k] = count
        count += 1
    
    numbers = ""
    
    for letter in text.lower():
        if letter in alphabet:
            new_number = alpha_index[letter]
            numbers = numbers + str(new_number) + " "

    return numbers.rstrip()
