# import sys

# n,k =int(sys.stdin.readline())

# def bin(n, k):
#     if (k==0 or n==k):
#         return 1
#     else:
#         return bin(n-1,k-1)+ bin(n-1,k)

# for i in range(11):
#     for k in range(n+1):
#         print(bin(n,k), end=" ")
#     print()

    #================================
# import math

# n,k=map(int, input().split())
# print(math.factorial(n)//(math.factorial(k)*math.factorial(n-k)))

#====================================================
from math import factorial 

n, k = map(int, input().split()) 
b = factorial(n) // (factorial(k) * factorial(n - k)) 
print(b)

# factorial(2)
# print(factorial(2))