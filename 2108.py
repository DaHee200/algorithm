# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 
# 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이

import sys
from collections import Counter

n=int(sys.stdin.readline())

save=[]

for _ in range(n):
    numbers=int(sys.stdin.readline())
    save.append(numbers)
save.sort()
#산술평균
a=round(sum(save)/n)
print(a)
#중앙값
print(save[n//2])

#최빈값
save_s=Counter(save).most_common()
#순서대로 정리
if len(save_s)>1:
    if save_s[0][1] == save_s[1][1]:
        print(save_s[1][0])
    else:
        print(save_s[0][0])
else:
    print(save[0])
    #범위
print(save[-1]-save[0])