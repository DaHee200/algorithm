# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 
# 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 
# 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

import sys
from collections import deque
n=int(sys.stdin.readline())
q=deque([])

def push(x):
    q.append(x)

def pop():
    if not q:
        return -1
    else:
        return q.popleft()

def size():
    return len(q)

def empty():
    if not q:
        return 1
    else:
        return 0

def front():
    if not q:
        return -1
    else:
        return q[0]
def back():
    if not q:
        return -1
    else:
        return q[-1]




for i in range(n):
    a=sys.stdin.readline().split()
    order = a[0]

    if order=="push":
        push(a[1])
    elif order=="pop":
        print(pop())
    elif order=="size":
        print(size())
    elif order=="empty":
        print(empty())
    elif order=="front":
        print(front())
    elif order=="back":
        print(back())
        #각 입력값의 함수를 만들어서 출력