#그리디 알고리즘 
#1. 탐욕스런 선택 조건(greedy choice proeprty)
#2. 최적 부분 구조 조건(optimal substructure)

#n=동전의 종류
#k=가치의 합
#A=동전의 가치
import sys

n, pay_coin = map(int, sys.stdin.readline().split())
#동전의 개수와 지불해야 하는 값을 받아 온다
coin_list=[]

for i in range(n):
        coin = int(sys.stdin.readline())
        #동전을 받아 온다
        coin_list.append(coin)
        #동전을 계산하기 위해 리스트에 넣는다

count=0
for i in reversed(range(n)):
# 숫자가 큰단위 부터 계산해 나간다
    count += pay_coin//coin_list[i]
    #coin_list안에 있는 동전들로 지불해야 하는 값이 나뉘어지는지 확인한다.
    pay_coin = pay_coin%coin_list[i]
    #위에는 몫만 가져오게 되어 있으니 지불해야하는 남은 값을 다시 pay_coin에 넣는다.

print(count)
