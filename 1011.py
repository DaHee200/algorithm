#처음에 1광년 이동하고 마지막에도 1광년으로 끝내야 한다
#일단은 n-1, n ,n+1중에 하나만 이동 가능하다
#거리가 주어 졌을때 최소의 이동 횟수로 도착하는 것을 구하라
# 각 이동 횟수에 따른 최대 거리를 구하라
#최대 이동 수를 구하라(그 수 안에서는 다 이동이 가능하니까)
# 이문제의 핵심 n값은 이동 테이블에서 가장 많이 이동한 광년
#n값을 이용해서 수열의 합 공식으로 최대값을 나타낼 수 있음
#b-a는 거리이다
#while문을 돌려 두 수의 차이보다 작은 제곱수 중에서 가장 큰 값을 찾는다
import sys
import math

T = int(sys.stdin.readline())
results=[]
#최소 횟수 규칙 홀수 n*2 짝수 n*2+n

for i in range(T):
    start, end = map(int, sys.stdin.readline().split())
    dist = end -start   
    #출발지와 도착지 사이의 거리 구함
    factor = math.ceil(math.sqrt(dist))
    #출발지와 도착지 사이의 거리의 제곱근 구하고 반올림
    #예를 들어 거리가 14이면 factor이 4이고
    
    flag1 = (factor -1) ** 2
    #factor-1의 제곱 / flag1은 9이고
    flag2 = factor ** 2
    #factor의 제곱 / flag2는 16이다

    if dist >= (flag1 + flag2) / 2: 
        #거리가 9와 16의 가운데를 나누면 12.5
        res = factor * 2 - 1
        
    
    else: res = factor * 2 - 2

    results.append(res)

for result in results:
    sys.stdout.write(str(result)+'\n')