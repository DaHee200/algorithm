#첫번째 줄에 단어의 개수 n이 들어온다 n<=100
#둘째줄에는 단어가 들어온다.
#첫째줄에 단어의 개수를 출력 한다.

import sys

N = int(sys.stdin.readline())

check =0
for i in range(N):
    number = 0
    alpha = sys.stdin.readline()
    for j in range(len(alpha)-1):
        #인덱스로 바꿔준다
        if alpha[j] != alpha[j+1]:
            #연달아 나오는 글자가 다를때
                alpha_list=alpha[j+1:]
            #첫글자를 뺀 나머지글자를 새로 만든다
                if alpha_list.count(alpha[j]) > 0:
                #남은 문자열에서 처음 나온 글자가 있으면 그룹 단어가 아니기 때문에                
                    number+=1
                #check에  +1을 한다
    if number == 0:
        check += 1
print(check)






# cnt =0
# for i in range(int(input())):
#     word = input()
#     cnt+=list(word) == sorted(word, key=word.find)
# print(cnt)

