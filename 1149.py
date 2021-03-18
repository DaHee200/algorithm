# 3
# 26 40 83
# 49 60 57
# 13 89 99

import sys

# n = sys.stdin.readline()

# for i in n:
#     arr.append(list(map(int, sys.stdin.readline())))    
# for j in range(1, len(p)):
    

#-------------------------------------------------------------
# 1149 RGB 거리
# 다이나믹 프로그래밍
#
 
n = int(sys.stdin.readline())
cost = [] # [[R1, G1, B1], [R2, G2, B2], ...]
 
# 집의 가격을 저장한다.
for _ in range(n):
    cost.append(list(map(int, sys.stdin.readline().split())))
 
 
dp = [cost[0]]   # dp = [[26, 40, 83]]
 
 
for i in range(1, n):
    cost_per_color = []
 
    #  (초록, 파랑)  | 빨강
    # 현재 빨강을 선택했을 때 최소 저장
    temp_red = min(dp[i - 1][1], dp[i - 1][2])
    #dp의 0번째 값을 선택했을때 dp[0][1]과 dp[0][2]값을 그대로 가지고 간다.
    cost_per_color.append(temp_red + cost[i][0])
    #그럼 빨간색으로 결정을 했으니 dp[0][0]번째 값과 dp[1][0]번째 값을 더한다.

 
    #  (빨강, 파랑)  | 초록
    # 현재 초록을 선택했을 때 최소 저장
    temp_green = min(dp[i - 1][0], dp[i - 1][2])
    cost_per_color.append(temp_green + cost[i][1])
 
    #  (빨강, 초록)  | 파랑
    # 현재 초록을 선택했을 때 최소 저장
    temp_blue = min(dp[i - 1][0], dp[i - 1][1])
    cost_per_color.append(temp_blue + cost[i][2])
 
    dp.append(cost_per_color)
 
print(min(dp[n - 1]))