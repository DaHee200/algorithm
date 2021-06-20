a,b=map(int, input().split())

if a <= 23 and b >= 45:
    return (a,b-45)
elif a > 23 :
    return (a - 1, b - 45)
