#stack에 push하는 순서 = 오름차순
import sys 

a = int(sys.stdin.readline())
count = 1
#count =1 반드시 오름차순으로 넣어야 하기 때문에
stack =[]
#수열을 담기 위해서
op=[]
temp = True
for i in range(a):
    number = int(sys.stdin.readline())
    #두번째 값 받기
    while count <= number:
        stack.append(count)
        op.append('+')
        count += 1
        #오름차순으로 값을 받아야 하니까  
        # 조건을 충족하면 1을 늘림
    if stack[-1]==number:
        stack.pop()
        op.append('-')
    else:
        temp = False
if temp == False:
    print('NO')
else: 
    for i in op:
        print(i)

