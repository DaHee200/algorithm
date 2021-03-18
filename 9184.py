
# #-50 ≤ a, b, c ≤ 50
#dp 큰 문제를 작은 문제로 나눠서 푸는 알고리즘으로 
# 분할 정복법(Divide and Conquer)과 유사하다
import sys



#0으로 초기화 된 3차원 배열 형태의 DP 테이블을 만든다
# a, b, c의 범위가 -50부터 50까지이지만 -는 1로 출력되기 때문에  
# a, b, c에 각각 50씩 더하여 전부 양의 인덱싱으로 바꿈

def again (a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if dp[a][b][c] :
        return dp[a][b][c]

    if a > 20 or b > 20 or c > 20:
        return arr([20][20][20]) 
    if a < b < c:
        dp[a][b][c] = again(a, b, c-1) + again(a,  b-1, c-1) - again(a, b-1, c)

    else:
        dp[a][b][c] = again(a-1, b, c) + again(a-1, b-1, c) + again(a-1, b, c-1) - again(a-1, b-1, c-1)

    return dp[a][b][c]

dp=[[[0 for i in range(51)] for j in range(51)] for k in range(51)]
while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == -1 and b ==-1 and c ==-1:
        #-1일 경우 입력 안됨
        break
    # print('w(%d, %d, %d' % (a, b, c, again(a,b,c)))
    print('w({0}, {1}, {2}) = {3}'.format(a, b, c, again(a,b,c)))


    #------------------------------------------------
    # 원동균 / 27조 /1436
# 파이썬 3차원 배열을 사용하는 방법을 배워봅시다.
# 일반적으로 numpy라는 애를 사용하는데, 알고리즘 시험에서는 못 사용하는 라이브러리 입니다.
# 그래서 메모이제이션 배열인 memo를 3차원으로 선언하고, 만약 좌표에 0이 하나라도 들어가 있다면 1로 초기화 하고 그렇지 않으면 0으로 초기화 했습니다.
# a,b,c값은 그 값에 해당하는 memo 배열에 저장하면 됩니다.
# 나머지는 피보나치 수열 동적 프로그래밍 방법처럼 하시면 됩니다.

# import sys

# memo = [[[0 for _ in range(51)]for _ in range(51)]for _ in range(51)]

# for i in range(51) :
#     for j in range(51) :
#         for k in range(51) :
#             if i == 0 or j == 0 or k == 0 :
#                 memo[i][j][k] = 1
#             else :
#                 memo[i][j][k] = 0

# def alg(a, b, c) :

#     if a <= 0 or b <= 0 or c <= 0 :
#         return 1        

#     if memo[a][b][c] != 0 :
#         return memo[a][b][c]

#     if a > 20 or b > 20 or c > 20 :
#         return alg(20, 20, 20)

#     if a < b and b < c :
#         memo[a][b][c] = alg(a, b, c-1) + alg(a, b-1, c-1) - alg(a, b-1, c)
#         return memo[a][b][c]


#     memo[a][b][c] = alg(a-1, b, c) + alg(a-1, b-1, c) + alg(a-1, b, c-1) - alg(a-1, b-1, c-1) 
#     return memo[a][b][c]


# arr = []
# answer = []
# while True :
#     x, y, z = map(int, sys.stdin.readline().split())
#     if x == -1 and y == -1 and z == -1 :
#         break
#     else :
#         arr.append([x, y, z])
#         answer.append(alg(x, y, z))

# for i in range(len(arr)) :
#     word = 'w({0}, {1}, {2}) = {3}'.format(arr[i][0], arr[i][1], arr[i][2], answer[i])
# print(word)