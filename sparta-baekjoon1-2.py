#----------------------10250--------------------------

# for _ in range(int(input())):
#     h, w, n = map(int, int().split())
#     a = n%h; b = n // h + 1
#     if a ==0 : a = h; b -= 1
#     print(a*100+b)
#-----------------1929------------------------
import sys
import math
m, n = map(int, sys.stdin.readline().split())

list = []
for i in range(m, n+1):
    if i == 3 or i == 2 or i == math.sqrt(i) :
        list.append(i)
    else:
        if i % 2 == 0 or i % 3 == 0 or i % 5 ==0 or i % 7 == 0:
            continue
        else:
            list.append(i)
print(list)
#----------------------11729-------------------------
import sys

n = int(sys.stdin.readline())

def hanoi(n, a, b, c):
    if n == 1:
        print(a, c)
    else:
        hanoi(n - 1, a, c, b)
        print(a, c)
        hanoi(n - 1, b, a, c)
sum = 1
for i in range(n - 1):
    sum = sum * 2 + 1
print(sum)
hanoi(n, 1, 2, 3)
