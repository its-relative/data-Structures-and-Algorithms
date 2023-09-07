# def printpattern(n):

#     for i in range(n):
#         print(i*"*".rjust(n))

n = int(input())

# pattern = printpattern(n)
for i in range(1,n,2):
    print(" "*(n-i-1),("*")*i)






