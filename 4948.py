# import sys

# n=int(sys.stdin.readline())
# a = [] 


# for i in range(n):
#     num=int(sys.stdin.readline())
#     for j in range(num):
#         if j%n==0:
#             break
#         else:
#             a.append(i)
# print(a)
#--------------------------------------------
# import math
# import sys

# def IsPrime(i):
#         if i ==1:
#             return True
#         else:
#             for j in range(2, int(math.sqrt(number))+1):
#                 if i % j == 0 :
#                     return False

#         return True


# # result = find_prime_list_under_number(input)
# # print(result)
# value=list(range(123456*2))
# prime_list=[]

# while True:
#     n = int(sys.stdin.readline())
#     if n == 0:
#          break
#     for number in value:
#         if IsPrime(number):  
#             prime_list.append(number)
            
#     for inside in prime_list:
#         cnt =0
#         if n< inside < n*2:
#             cnt += 1
#     print(cnt)

#---------------------------------------------
import math
import sys

def isPrime(num):
    if num == 1: 
        return False
    a =int(math.sqrt(num))
    for i in range(2, a+1):
        #2의 제곱근 1.414..../ 7의 제곱근 2.645...
        if num % i == 0: 
            return False

    return True

li = list(range(2,246912))
#1,2,3,4,5,6의 수들 중에서 소수들을 구하라
arr = []
#소수들 리스트
for i in li:
    if isPrime(i):
        arr.append(i)

while(1):
    answer = 0
    n = int(sys.stdin.readline())
    if n == 0: break

    for i in arr:
        if n < i <= n*2:
            answer += 1
            #범위 내에 있는 숫자 카운트

    print(answer)