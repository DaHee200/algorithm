import sys

k=int(sys.stdin.readline())
A=[]      
#리스트에 저장하기

for i in range(k):
    n = int(sys.stdin.readline())
    if n == 0:
        A.pop()
        #0이 들어오면 그전에 최근 수를 지운다
    else:
        A.append(n)
        #0이 아니라면 받은 값을 리스트에 저장한다
print(sum(A))
#더한 값을 출력한다