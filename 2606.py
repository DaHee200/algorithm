#---------------------------------------------------------------------
from sys import stdin
#bfs방식의 문제 풀기
read = stdin.readline
#컴퓨터의 수 입력 받기
dic={}
for i in range(int(read())):
#read의 범위 만큼 i를 돌려라
    dic[i+1] = set()
    #컴퓨터 1, 컴퓨터 2, 컴퓨터3 각각의 리스트를 만들어 주기 위해서 
    #그리고 중복 되는 수가 없게 하기 위해서 set()함수를 사용
for j in range(int(read())):
    #read의 범위 만큼 i를 돌려라
    a, b = map(int, read().split())
    #네트워 상에서 직접 입력되어 있는 컴퓨터 쌍의 수
    dic[a].add(b)
    dic[b].add(a)
    #각 컴퓨터의 리스트 안에 연결되어 있는 컴퓨터 리스트 들을 저장 한다

def dfs(start, dic):
    for i in dic[start]:
        #dic값을 돌려서 중복되는 값을 제거하여 수가 중복 되지 않도록 하는 작업
        if i not in visited:
            visited.append(i)
            #visited에 들어가 있지 않으면 거쳐 가지 않은 것으로 
            #visited값에 더해 준다
            dfs(i, dic)
visited = []
dfs(1, dic)
print(len(visited)-1)

#7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7