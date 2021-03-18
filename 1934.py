#첫째줄에 테스트 케이스
#둘째줄부터 

# import sys

# t = map(int, sys.stdin.readline())

# def gcd(a, b) :
#     if b==0:
#         return a
#     else :
#         return gcd(b,a%b)

# def lcm(a, b) :
#     g = gcd(a,b)
#     #b가 0일때 a값만 return하니까 g=6이 된다
#     return int(g*(a/g)*(b/g))

# for i in range(t):
#     a, b = map(int, sys.stdin.readline().split())
    #---------------------------------------
import sys

def GCD(a,b):
    while b!=0:
        r = a%b
        a = b
        b = r
    return a
    #A를 B로 나누고 남은 몫을 r로 가지고 와서 b가 0이 될때 까지 나눠 줍니다.
def LCM(a,b):
    #Least Common Multiple
    return a*b//GCD(a,b)


for _ in range(int(sys.stdin.readline())):
    a,b = map(int, sys.stdin.readline().split())

    print(LCM(a,b))
    
