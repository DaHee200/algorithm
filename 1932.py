#선택된 수의 합이 최대가 되는 수를 구하여랴
# 아래층에 있는 수는 현재 층에서 선택된 수의
#  대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.
#1<삼각형의 크기<500
#0<범위<9999

import sys

n=int(sys.stdin.readline())
#줄의 값을 받는다

result=[]
#계산된 줄의 값을 저장 한다

for _ in range(n):

    numbers=list(map(int, sys.stdin.readline().split()))
    #줄의 숫자들을 받는다
    result.append(numbers)
    #줄의 숫자들을 result에 저장 한다

dp = []

for i in range(1, n):
    for j in range(len(result[i])):
        if j == 0:
            result[i][j] += result[i-1][j]
            #0번째줄 0번째와 1번째줄 0번째를 더한 값을 1번째줄 0에 넣어 줍니다.
        elif j == len(result[i]) - 1:
            result[i][j] += result[i-1][j-1]
            #0번째줄 0번째와 1번째줄 1번째를 더한 값을  1번째줄 1에 넣어 줍니다.
            #내려오는 값과 오른쪽에 있는 값을 더해야 하니까 j, j-1로 계산해 줍니다.
        else:
            result[i][j] += max(result[i-1][j-1], result[i-1][j])

print(max(result[n-1]))
#최대 값을 출력 한다

print(result)




    
