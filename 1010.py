import sys

s=[[0]*30 for i in range(30)]
for i in range(1,30):
    s[1][i]=i
    #예시 01:[0, 1, 2, 3, 4, 5, 6, 7, 8, 9,  ...]
    #n이 1일때는 m과 같다
for i in range(2,30):
    #2번째줄부터
    for j in range(1,30):
        #2번째줄의 1번째부터 경우의 수 
        for k in range(i-1,j):
            #예시 02:[0, 0, 1, 1, ...]
            s[i][j]+= s[i-1][k]
        #s의 i번째 줄의 j번째 값에 s[i-1]줄의 k값을 더한다

t=int(sys.stdin.readline())
for i in range(t):
    n,m=map(int, sys.stdin.readline().split())
    print(s[n][m])
    #0부터 30까지 값들중에 주어지는 조건에 대해서 값을 출력 한다.

