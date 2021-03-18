#최대 공약수= Greatest Common Divisor
#최소 공배수 = Least Common Multiple
#모듈로(Modulo) %
import sys

a, b = map(int,sys.stdin.readline().split())

def gcd(a, b) :
    if b==0:
        return a
    else :
        return gcd(b,a%b)
       

def lcm(a, b) :
    g = gcd(a,b)
    #b가 0일때 a값만 return하니까 g=6이 된다
    return int(g*(a/g)*(b/g))

print(gcd(a, b)) 
print(lcm(a, b))
