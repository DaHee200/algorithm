#첫 삼각형은 정삼각형으로 변의 길이는 1이다. 
#P(n)은 나선에 있는 정삼각형의 변의 길이이다. 
#프린트 안에 함수 사용하여 프린트
# P(n)=P(n-2)+(n-3)
# from sys import stdin

# t = stdin.readline()

# memo={1:1, 
#      2:1, 
#      3:1
#      }

# def count_number(a):
#     if a in memo:
#         return memo
#     else:
#         cont=(a-2)+(a-3)
#         return cont

#     print(memo(a))
    
# # #---------------------------------------
# import sys

# t = int(sys.stdin.readline())#t 값을 넣고 그다음 코드들이 빠져있네요?


# memo={1:1, 
#     2:1, 
#     3:1
#     }

# def number(a):
#     if a in memo: #n은 어디서 나온거죠? 딴거 넣으세요
#         return memo[a]
#     else:
#         count = number(a-2)+number(a-3) #함수가 빠져있네요?
#         #cont값을 memo에 넣어주세요~
#         memo[a]=count
#         return count

# for i in range(t):
#     n = int(sys.stdin.readline())
#     print(number(n)) #memo가 아니죠?
    #=================================================
import sys

t = int(sys.stdin.readline())

memo={1:1, 
    2:1, 
    3:1

    }

def number(a):
    if a in memo: 
        return memo[a]
    else:
        count = number(a-2)+number(a-3) 
        memo[a]=count
        return count

for i in range(t):
    n = int(sys.stdin.readline())
    print(number(n)) 