
# # 브루트포스 - 쉽게 말하면 싹다 뒤지는 알고리즘
# # 브루트포스 문제라서 정말로 무식하게 풀었습니다.
# # 이 문제는 6이 3개 이상 붙어있어야 합니다. 딱 666만 찾는 문제가 아닙니다.
# # 일단 첫번째 666은 무조건 666이란 수이기 때문에 arr에 담았습니다.
# # 그리고 두번째 666은 1666이기 때문에 1665부터 시작했습니다.
# # 그래서 find문으로 '666'이란 수가 존재하면 반복문을 돌면서 카운트 값을 증가시킵니다.
# # 만약 카운트 값이 3보다 크거나 같으면 배열에 담아줍니다.


import sys

n = int(sys.stdin.readline().split()[0])
array = [666]
number = 1665

if n == 1 :
    print(array[0])
else :
    while True :
        number += 1
        cnt = 0
        if str(number).find('666') != -1 :
            a = list(str(number))
            for i in range(len(a)) :
                if i > 0 :
                    if a[i] == '6' :
                        if a[i-1] == '6' :
                            cnt += 1
        if cnt >= 2:
            array.append(int(''.join(a)))
        if len(array) == n :
            print(array[-1])
            break

# array=[666,1666,2666,6666,66666]
# for i in array:
#     a=str(i)
#     if a.find('666')==True:
#         print('yes')