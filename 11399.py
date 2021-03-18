# 5
# 3 1 4 3 2

import sys

n = int(sys.stdin.readline())

times = list(map(int,sys.stdin.readline().split()))
times.sort()
#오름차순으로 되어 있는 숫자를 반대로 정렬
wait=0
#기다리는 시간
total=0
#총합 시간
for i in times:
    wait += i
    #시간을 더한다
    total += wait
    #더한 시간을 내용물로 옮깁니다.
print(total)