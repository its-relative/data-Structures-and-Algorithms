# Write a function that returns the sum of the first n natural numbers,
# where a natural number is a positive integer.
# For example, sum_n(3) should return 6 and sum_n(10) should return 55. 
# Use the if name = “main” block to test your function with some examples.

def summer(num):
    return int((num*(num+1))/2)

if __name__ == "__main__":
    n = int(input("Enter the number: \t"))
    x = summer(n)
    print(x)