# 분할 정복 : 재귀적으로 자신을 호출하면서 그 연산의 단위를 
# 조금씩 줄여가는 방식
import sys

n = int(sys.stdin.readline())

paper=[list(map(int, sys.stdin.readline().split()))for _ in range(n)]

save=[]

def process(x, y, n):
    color=paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color !=paper[i][j]:
                process(x,y,n//2)
                process(x, y+n//2, n//2)
                process(x+n//2, y, n//2)
                process(x+n//2, y+n//2, n/2)
                return
    if color == 0:
        save.append(0)
    else:
       save.append(1)

process(0,0,n)
print(save.count(0))
print(save.count(1))

#======================================================
# from sys import stdin
# read = stdin.readline
# N = int(read())
# lst = []
# for _ in range(N):
#   lst.append(list(map(int, read().split())))
# print(lst)
# def conqure(n, lst):
#   # 이중 리스트안에 1이 없으면 조건충족
#   if not any(1 in i for i in lst):
#     # 함수안에서 전역변수값을 가지고 쓸 때 전역변수 값을 변형시킬려면 global을 써야한다.
#     global cnt_0 
#     cnt_0 += 1
#     return
#   # 이중 리스트안에 0이 없으면 조건충족
#   elif not any(0 in i for i in lst):
#     global cnt_1
#     cnt_1 += 1 
#     return
#   else:
#     lst_0 = []
#     lst_1 = []
#     for i in lst:
#       lst_0.append(i[:n//2])
#       lst_1.append(i[n//2:])
#     conqure(n//2, lst_0[:n//2])  
#     conqure(n//2, lst_0[n//2:]) 
#     conqure(n//2, lst_1[n//2:]) 
#     conqure(n//2, lst_1[:n//2])
#     return


# cnt_0 = 0
# cnt_1 = 0
# conqure(N, lst)
# print(cnt_0)
# print(cnt_1)