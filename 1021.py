# # import collections

 

# # # Create a deque from the tuple
# # sequenceInDeque = collections.deque(sequence)


# # # Rotate once - in negative direction(오른쪽으로 넘기기 1은 갯수)
# # sequenceInDeque.rotate(-1)

# #------------------------------------------
# import sys
# # import queue
# # from collections import deque
# # #양방향 큐의 기능 지원 rotate
# # #무조건 데크에서만 지원 한다
# # #양방향 키 덱
#     q.append(i)
#     #스택이나 큐처럼 덱의 오른쪽에서 요소 삽입

# q.appendleft()
# #덱의 왼쪽에서 요소 삽입
# q.insert()
# #덱 중간에 요소 삽입
# rotate()
# #큐에서만 사용 가능 양수(1)쓰면 오른쪽 음수(-1) 넣으면 왼쪽
# #l값은 고정이지만 r값은 변동되다. 데크의 크기가 조정 되기 때문에
# # --------------------------------------------------------------------------------
# import collections

# max_num, target_num = map(int, input().split())
# target_list = list(map(int, input().split()))
# que = collections.deque([i for i in range(1, max_num +1)])
# result = 0

# for num in target_list:
#     if num == que[0]:
#         que.popleft()
#         continue
#     left_move = que.index(num)
#     right_move = len(que) - left_move
    
#     if left_move <= right_move:
#         que.rotate(-left_move)
#         que.popleft()
#         result += left_move
#     else:
#         que.rotate(right_move)
#         que.popleft() 
#         result += right_move
        
# print(result)
# //-------------------------------------------------------------------------------
2606
import sys
from collections import deque
n,m = map(int, sys.stdin.readline().split())
#큐의 크기 = n, 뽑아내려는 수의 개수 = m
numbers=list(map(int, sys.stdin.readline().split()))
#numbers는 뽑아내려고 하는 수의 위치
queue = deque(range(1, n+1))
#양방향움직임이 가능하게 하기 위해서 덱을 써줌

total = 0
#몇번만에 뺐는지 카운트하기 위한 변수
for i in range(len(numbers)):
    #numbers길이의 범위 만큼 돌아라
    if numbers[i] == queue[0]:
        #뽑아 내려는 수와 큐 0번째의 위치가 같다면 바로 뽑을 수 있다
        queue.popleft()
        #왼쪽에서 값을 뽑아 낸다 
        continue
    queue_n = queue.index(numbers[i])
    #numbers의 숫자의 index를 알려 준다

    if queue_n > len(queue) // 2:
        #찾으려는 수의 인덱스 넘버와 켜의 길이를 반으로 자른 수를 계산 한다
        queue.rotate(len(queue)-queue_n)
        #위 의 조건을 충족하면 2를 빼기 위해 1을 오른쪽으로 넘겨 줘야 하니까
        #rotate를 사용하여 1을 뒤로 넘겨 주고 2를 뺀다
        total += (len(queue)-queue_n)
        #
    elif queue_n <= len(queue)//2:
        #n의 인데스 넘버가 큐의 총길이의 1/2값보다 작으면 
        #앞에서 뒤로 옮겨야 최소값을 구할 수 있다.
        queue.rotate(-queue_n)
        #rotate는 음수를 넣어야 왼쪽으로 회전하기 때문에 음수를 넣는다
        total += queue_n
        #카운트를 해준다
    queue.popleft()
    #찾은 값을 뺀다

print(total)