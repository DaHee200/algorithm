import sys

n = int(sys.stdin.readline())

for i in range(n-1) :
    a = list(map(int, sys.stdin.readline().split()))

    c=max(a)
    d=min(a)

    print(c*d)


