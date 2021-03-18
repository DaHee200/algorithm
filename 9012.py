import sys 

n= int(sys.stdin.readline())

for i in range(n):
    ps = sys.stdin.readline()
    c=list(ps)
    sum =0
    for i in c:
        if i =="(":
          sum +=1
          #리스트 안에 열리는 가로가 있으면 더하고
        elif i ==")":
            sum -= 1
            #닫히는 가로이면 뺀다
        if sum<0:
            print('NO')
            break
        # print(sum)

    if sum > 0:
        print('NO')
    elif sum==0:
        print('YES')



        #====================================
# a = int(input())
# for i in range(a):
#     b = input()
#     s = list(b)
#     sum = 0
#     for i in s:
#         if i == '(':
#             sum += 1
#         elif i == ')':
#             sum -= 1
#         if sum < 0:
#             print('NO')
#             break
#     if sum > 0:
#         print('NO')
#     elif sum == 0:
#         print('YES')

        

