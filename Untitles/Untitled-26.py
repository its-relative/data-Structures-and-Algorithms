# Question: Sum of Digits
# 
# Write a Python function to calculate the sum of the digits of a positive integer using a while loop.

# Code goes here
def sum_of_digits(n):
    linum = list(str(n))
    count = 0
    it = 0
    while it < len(linum):
        count += int(linum[it])
        it += 1

    return count

# Sample Input and Output
num = 12345
result = sum_of_digits(num)
print("Sum of digits in", num, "is", result)  # Output: Sum of digits in 12345 is 15
