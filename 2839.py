import sys

N = int(sys.stdin.readline())
count =0
if N % 5 ==0:
    #N을 5로 나눈 나머지가 없게 되면 값이 딱 떨어지니까 
    count = int(N//5)
    #포대 수는 몫이 된다
else:
    while True:
        N -=3
        #if조건을 충족하지 못할 경우
        #N에서 3을 뺀다
        count += 1
        #뺀 횟수 만큼 숫자를 카운트 한다
        if N%5 ==0:
            #만약에 3을 빼는 사이에 5로 딱 나누어 떨어지면
            count += int(N//5)
            #그 몫을 포대수에 카운트 한다
            break
        elif N < 2:
            #만약에 N의 수가 2보다 작게 되면 3보다 작은 포대가 없기 때문에
            # 계산을 할 수 없게 된다. 그럼 문제에 따라서 -1을 출력 해야 하므로
            #포대 수(count)는 -1일이 된다
            count = -1
print(count)


