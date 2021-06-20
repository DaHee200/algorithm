
#-----------sparta python Question(Basic01)------------
# a = 24
# b = 16
# c = 26

# result = (a + b + c) / 3
# print(result)

#-----------sparta python Question(Basic02)------------
# a = "sparta"

# print (a[:3])
#------------parta python Question(Basic03)------------
# phone = "02-123-1234"
# result = phone.split('-')
# print(result[0])
#------------parta python Question(Basic04)------------
# people = [
#     {'name': 'bob', 'age': 20, 'score':{'math':90,'science':70}},
#     {'name': 'carry', 'age': 38, 'score':{'math':40,'science':72}},
#     {'name': 'smith', 'age': 28, 'score':{'math':80,'science':90}},
#     {'name': 'john', 'age': 34, 'score':{'math':75,'science':100}}
# ]
# print(people[2]["score"]["science"])

#------------parta python Question(Basic05)------------
# people = [
#     {'name': 'bob', 'age': 20},
#     {'name': 'carry', 'age': 38},
#     {'name': 'john', 'age': 7},
#     {'name': 'smith', 'age': 17},
#     {'name': 'ben', 'age': 27},
#     {'name': 'bobby', 'age': 57},
#     {'name': 'red', 'age': 32},
#     {'name': 'queen', 'age': 25}
# ]
# for i in people:
#     if i['age'] > 20:
#         print(i['name'])
#------------parta python Question(Basic06)------------
# -*- coding: utf-8 -*-
# fruits = ['사과', '배', '감', '귤','귤','수박','참외','감자','배','홍시','참외','오렌지']
# for i, fruit in enumerate(fruits):
#     print(i, fruit)
#     if i == 4:
#         break
#------------parta python Question(BasicTest01)------------
# max = 0
# num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]
# for number in num_list:
#     if number > max:
#         max = number
# print(max)
#------------parta python Question(BasicTest02)------------
def check_gender(pin):
    sex = pin.split('-')[1][0]
    if int(sex) % 2 == 0:
        print ("여자")
    else : 
        print("남자") 
    # print(int(sex))

my_pin = '200101-3012345'
check_gender(my_pin)

#--------------backjoon-----------
# import sys

# H, M = sys.stdin.readline().split()

# if M < 45:
#     H - 1
# elif H == 0:
#     H == 23
#     M + 15
#         print(H, M) 
