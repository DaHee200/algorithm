# import sys
# M, N = map(int, sys.stdin.readline())
# count=[]

# def dfs(start, last):


# for i in range(N):
#     T = map(int, sys.stdin.readline())
#     for j in range(T):
#         if j ==
#------------------------------------------------------
# from collections import deque

# dx = [1, -1, 0, 0]
# #x좌표를 구하기 위해 선언
# #상하좌우만 판단하면 됨
# #동서남북
# dy = [0, 0, 1, -1]
# #y좌표를 구하기 위해 선언

# def bfs():
#     result = 0
#     while q:
#         result += 1
#         for _ in range(len(q)):
#             x, y = q.popleft()
#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#                 if 0 <= nx < n and 0 <= ny < m:
#                     if a[nx][ny] == 0:
#                         a[nx][ny] = 1
#                         q.append([nx, ny])
#     return result

# m, n = map(int, input().split())
# a, q = [], deque()
# for i in range(n):
#     row = list(map(int, input().split()))
#     for j in range(m):
#         if row[j] == 1:
#             q.append([i, j])
#     a.append(row)

# result = bfs() - 1
# for i in range(n):
#     for j in range(m):
#         if a[i][j] == 0:
#             print(-1)
#             exit()
# print(result)
#-------------------------------------------------------------------
import sys
from collections import deque
 
m, n = map(int, sys.stdin.readline().split())
 
arr = []
tmtDeque = deque()
 
for i in range(n) :
    arr.append(list(map(int, sys.stdin.readline().split())))
    for j in range(m) :
        if arr[i][j] == 1 :
            tmtDeque.append([i, j])
 
 
def tmtDeqAlg(hori, verti, tmtBox) :
    day = -1;    
    locX = [0, 0, 1, -1]                   # x 및 y의 좌표 설정
#상,하,좌,우
#      2,5
# 3,4<-3,5->3,6
#      4,5
    locY = [-1, 1, 0, 0]
#  q=[3,5] ->2,5
    while tmtDeque :
        day += 1
        
        # tmtDeque 크기 만큼 돌면서 다 익은 토마토 위치를 pop하고, 그 주변 토마토가 익지 않았다면 그걸 다시 데크에 넣고 1로 바꿈
        # 즉, 이 코드는 값이 1인 애들이 데크에 존재하고 그 주변에서 0인 애들을 데크에 넣고 1로 바꾼 다음에 바뀐 애들의 위치를 데크에 넣고 돌리는 것임! 
        for _ in range(len(tmtDeque)) :
            tmtloc = tmtDeque.popleft()
            for j in range(4) :
                tmtX = tmtloc[1] + locX[j] 
                tmtY = tmtloc[0] + locY[j] 
 
                if (0 <= tmtX < m) and (0 <= tmtY < n) :
                    #토마토의 범위가 상자 범위 밖을 넘어 가지 않도록 범위를 정해 놓음
                    if tmtBox[tmtY][tmtX] == 0 :
                        tmtDeque.append([tmtY , tmtX]) 
                        tmtBox[tmtY][tmtX] = 1
 
    for i in range(n) :
        for j in range(m) :
            if arr[i][j] == 0 :
                return -1
 
    return day
 
print(tmtDeqAlg(m, n, arr))