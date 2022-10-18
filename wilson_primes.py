# Wilson primes satisfy the following condition. Let P represent a prime number.
# Then,
# ((P-1)! + 1) / (P * P)
# should give a whole number.
#
# Your task is to create a function that returns true if the given number is a Wilson prime.
# Python 3.10, kyu 8
#
# Note: it works but... error: "Execution Timed Out (12000 ms)"

def am_i_wilson(n):
    n_sum = 1
    if n > 1:
        for i in range(n):
            if i != 0:
                n_sum = int(n_sum * i)

        if ((n_sum + 1)%(n)) == 0:
            return True
        else:
            return False
    else:
        return False
