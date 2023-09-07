# Write a function that checks if a number is prime and returns True or False. 
# For example, is_prime(17) should return True and is_prime(12) should return False. 
# Use the if name = “main” block to test your function with some examples.

def prime(n):
    isprime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(i)
            isprime = False
        else:
            isprime=True
    return isprime

if __name__ == "__main__":
    n = int(input())
    print(prime(n))
    

