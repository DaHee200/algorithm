# 1. 대문자나 소문자로 바꾸기 
# 2. 중복되는 글자 제거하기 
# 3. 원래 단어에서 글자 수 체크하기
# 4. 중복되는 글자 수가 두개 이상이면 ?를 출력하고 한개이면 글자를 출력한다. 
#--------------------1157----------------
# value = input().upper()

# word = list(set(value))
# cnt=[]
# for i in word:
#     cnt_num = value.count(i)
#     cnt.append(cnt_num)
    
# if cnt.count(max(cnt)) > 1 :
#     print('?')
# else :
#     max_index = cnt.index(max(cnt))
#     print(word[max_index])
#---------------------2941-----------------------
# alpha = [ 'c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=' ]
# word = input()

# for i in alpha:
#     word = word.replace(i, '*')
#     print(word)
    
# print(len(word))

#-----------------------2869-----------------------------
#1. 낮에는 나무를 올라간다. 
#2. 밤에는 일정 거리만큼 떨어진다. 
#3. 
A, B, V = map(int,input().split())

if (V-A)%(A-B) == 0:
    print(int((V-A)/(A-B))+1)
else:
    print(int((V-A)/(A-B))+2)
# morning, night, len = map(int, input().split())

# total = len
# day =0
# one_day = 0
# for i in range(len(total)):
#     if total > 0:
#         one_day = total-morning
#         print("one_day =", one_day )
#         if one_day > 0:
#             whole_day = one_day + night
#             print("whole_day=", whole_day)
#             total = whole_day
#             day += 1
#     else:
#         print(day)
