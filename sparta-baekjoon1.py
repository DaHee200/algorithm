import sys

# n = int(sys.stdin.readline())

# check = n
# newnumber = 0
# count = 0
# a = 0

# while True:
#     a = n//10 + n%10
#     newnumber = (n*10) + a%10
#     count += 1
#     n = newnumber
#     if check == newnumber:
#         break
# print(count)
#----------------------4344----------------

# n = int(sys.stdin.readline())

# for _ in range(n):
#     nums = list(map(int, sys.stdin.readline().split()))
#     avg = sum(nums[1:]) / nums[0]
#     cnt =0
#     for score in nums[1:] :
#         if score > avg:
#             cnt += 1
            
#     rate = cnt / nums[0] *100
#     print(f'{rate:.3f}%')
#-------------4673------------------
natural_num = set(range(1,10001))
generated_num = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    generated_num.add(i)
    
    
self_num = sorted(natural_num - generated_num)
for i in self_num:
    print(i)
