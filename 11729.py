# # 하노이의 탑 # 
# # 입력: 옮기려는 원반의 갯수 n
#  # 옮길 원반이 현재 있는 출발점 기둥 from_pos 
# # 원반을 옮길 도착점 기둥 to_pos 
# # 옮기는 과정에서 사용할 보조 기둥 aux_pos
#  # 출력: 원반을 옮기는 순서 
# def hanoi(n, from_pos, to_pos, aux_pos): 
#     if n == 1: 
# # 원반 한 개를 옮기는 문제면 그냥 옮기면 됨 
#         (from_pos, "->", to_pos) 
#         return 
# # 원반 n - 1개를 aux_pos로 이동(to_pos를 보조 기둥으로) 
#     hanoi(n - 1, from_pos, aux_pos, to_pos) 
# # 가장 큰 원반을 목적지로 이동 print(from_pos, "->", to_pos) 
# # aux_pos에 있는 원반 n-1개를 목적지로 이동(from_pos를 보조 기둥으로) 
#     hanoi(n - 1, aux_pos, to_pos, from_pos) 
# print("n = 1") 
# hanoi(1, 1, 3, 2) 
# # 원반 한 개를 1번 기둥에서 3번 기둥으로 이동(2번을 보조 기둥으로) print("n = 2") 
# hanoi(2, 1, 3, 2) # 원반 두 개를 1번 기둥에서 3번 기둥으로 이동(2번을 보조 기둥으로) 
# print("n = 3") 
# (3, 1, 3, 2) # 원반 세 개를 1번 기둥에서 3번 기둥으로 이동(2번을 보조 기둥으로)

# -----------------------------------------------------------------------------------------------------------------
# import sys

# move =[]
#             # 시작    도착
# def hanoi(n, dep, b, arr):
#             #  1  2  3
#         # n=2  1  3  2
#         # n=1  1  1  3
#     if n==1:
#         move.append([dep,arr])
#         # print(n, dep,arr)
#         # print('////////')
#     else:
#         hanoi(n-1,dep,arr,b)
#             #  2   1  3  2 
#             #  1   1  2  3 가장위의 원반 도착 지점이 막대기 2가 목적지라서 
#         # print(n, dep,arr)
#         # print('---------')
#         move.append([dep,arr])
#         hanoi(n-1,b,dep,arr)
#         # print('==============================')
#         # print(n-1, dep, arr)

# a=int(sys.stdin.readline())
# hanoi(a,1,2,3)
# print(len(move))
# print('\n'.join([' '.join(str(i) for i in row )for row in move]))
# #move안에 있는row안에 있는 i를 문자열로 변환하고 그 사이에 있는
# #','를
#-----------------------------------------------------------------

import sys

move =[]
#원판이 움직였을때 위치 값을 담아주기 위해서 리스트를 만듭니다.

          # 시작  도착
def hanoi(n, A, B, C):
       #     1  2  3
       # n=2 1  3  2
       # n=1 1  1  3
    if n==1:
        move.append([A,C])
        #원판이 한개 남았을때 움직인 값을 move에 저장합니다.
    else:
        hanoi(n-1,A,C,B)
        #n-1 = 2  1 3 2 
        #n-1 = 1  1 2 3 
        move.append([A,C])
        #움직인 값을 move에 저장합니다.
        hanoi(n-1,B,A,C)
        #그 다음 원판을 계산하기 위해 다시 하노이 함수를 호출합니다.
a=int(sys.stdin.readline())
#원판의 개수를 받는다
hanoi(a,1,2,3)
#하노이 함수를 호출한다
print(len(move))
#옮긴 횟수를 프린트하기 위해 move의 길이를 출력하여 줍니다.
print('\n'.join([' '.join(str(i) for i in row )for row in move]))
#move안에 있는 수(i, row)들을 문자열로 바꾸고 띄어쓰기를 넣고 줄을 바꿔 프린트 합니다.