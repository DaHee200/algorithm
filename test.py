# import sys

# N = int(sys.stdin.readline())
# #상근이가 가지고 있는 숫자 카드의 개수
# cnt1=list(map(int, sys.stdin.readline().split())) 
# M = int(sys.stdin.readline()) 
# cnt2=list(map(int, sys.stdin.readline()))

# cnt1.sort()

# #상근이가 가지고 있는 숫자 카드인지 아닌지를 구해야 할 개수
# for i in range(M):
#     low=0
#     high=N-1
#     while low<=high:
#     # def number(low, hight):
#         mid = (low + high) // 2
#         if cnt1[mid] == cnt2[i]:
#             print(1, end='')
#             break
#         elif cnt1[mid] > cnt2[i]:
#             high = mid -1
#             break
#         elif cnt1[mid] < cnt2[i]:
#             low = mid + 1
            
#         if low> high:
#             print(0, end='')
#             break


# for i in range(M): 
#     low = 0
#     high =N-1 
#     while low <= high: 
#         mid = (low + high) // 2 

#         if low > high: 
#             print(0, end=" ") 
#             break
        
#         if cnt1[mid] == cnt2[i]: 
#             print(1, end=" ") 
#             break 
#         elif cnt1[mid] < cnt2[i]: 
#             low = mid + 1 
#         else: 
#             high = mid - 1 
#             #----------------------------------------------------------------------------
# from collections import deque
# import sys

# N = int(sys.stdin.readline())
# deque = deque()

# for i in range(N):
#  deque.append(i+1)
# while not (len(deque) == 1):
#     #큐의 길이가 1이 아니면 while을 계속 돌려라
#     deque.popleft()
#     # 맨 앞의 숫자를 뒤로 옮기자.
#     back = deque.popleft()
#     #popleft는 왼쪽으로 숫자를 붙이는 것
#     deque.append(back)
#     #앞에 있는 숫자를 뒤에 가져다 붙이기
    
# print(deque[0])

# #--------------------------------------
#이진 탐색

# input = [3, 5, 6, 1, 2, 4]


# def find_max_num(array):
#     for i in array:
#         for j in array:
#             if i >vj:
#                 return find_max_num
#             else:
#                 return False
#     return 1


# result = find_max_num(input)
# print(result)







# import sys 
# from collections import deque

# N = int(sys.stdin.readline().split()[0]) 

# card=deque()
#  for i in range(1, N+1):
#      card.append()
# num=0
# while len(card)!= 1:
#     if num == 0 : 
#         card.popleft() 
#         num += 1
#     elif num % 2 != 0 : 
#         card.rotate(-1) 
#         num += 1 
#     else : 
#         card.popleft() 
#         num += 1
#         print(card[0])
#     back = queue.popleft()
#     deque.append(back)

#     rotate



# ==============================

# import sys 

# n = int(sys.stdin.readline())

# numbers = [] 
# for i in range(n) :
#     m = int(sys.stdin.readline()) 
#     numbers.append(m) 
#     numbers.sort() 
# for i in numbers : 
#     print(i)

#================================
# a,b = map(int, input().split())

# if a > b:
#     print('>')
# elif  a < b:
#     print('<')
# elif a==b:
#     print('==')
#====================================================

# n = int(input())

# if 90 <= n <=100:
#     print('A')
# elif 80<= n <=89:
#     print('B')
# elif 70<= n <=79:
#     print('C')
# elif 60<= n <=69:
#     print('D')
# else:
#     print('F')
#===============================
#윤년이면 1 아니면 0

# n=int(input())

# if n%4 == 0 and n%100!=0 or n%400==0:
#     print(1)
# else:
#     print(0)
#===================================
#14681 사분면 나타내기

# n = int(input())
# m = int(input())

# if n > 0 and m > 0:
#     print(1)
# elif n < 0 and m > 0:
#     print(2)
# elif n < 0 and m < 0:
#     print(3)
# elif n > 0 and m < 0:
#     print(4)
#===========================================
# 2884 알람시계
# n, m = map(int, input().split())

# if m < 45:
#     h = n-1
#     minute = m+15
#     if n == 0:
#         h=23
#     print(h,minute)

# elif m >= 45:
#     minute = m - 45
#     print(n,minute)

#==============================================
# 2739 구구단

# n = int(input())

# for i in range(1, 10):
#     c = n*i
#     print(n,'*',i, '=',c)

#=============================================
#10950 A+B-3

# t=int(input())

# for i in range(t):
#     a,b=map(int,input().split())
#     print(a+b)
#==============================
# 8393 합

# n = int(input())
# s=0
# for i in range(1, n+1):
#     s +=i
# print(s)
#===============================
# 15552 빠른A+B
# import sys

# t=int(sys.stdin.readline())

# for i in range(t):
#     n,m=map(int,sys.stdin.readline().split())
#     c=n+m
#     print(c)
#============================
# 2741 n찍기
# n=int(input())
# for i in range(1, n+1):
#     print(i)
#=========================
# 2742 기찍n
# n=int(input())

# for i in reversed(range(1, n+1)):
#     print(i)
#==============================
#11021 

# n=int(input())

# for i in range(1, n+1):
#     n,m=map(int,input().split())
#     c=n+m
#     print('Case #%d: %d' %(i,c))

#======================================
# 11022

# n=int(input())

# for i in range(1, n+1):
#     n,m=map(int, input().split())
#     c=n+m
#     print('Case #%d: %d + %d = %d' %(i,n,m,c))
#==================================
# 2438 별찍기

n=int(input())

for i in range(1,n+1):
    print()