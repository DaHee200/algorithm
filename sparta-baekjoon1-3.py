#-------------11651---------------
import sys
n = int(sys.stdin.readline())

a =[]
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    rev = [y,x]
    a.append(rev)
    print("rev=", rev)
b = sorted(a)
print("b=", b)
for i in range(n):
    print(b[i][1], b[i][0])