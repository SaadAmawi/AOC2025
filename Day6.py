import math
with open("Day6.txt","r")as f:
    input = list(fa.split() for fa in f.read().split('\n'))

# print(input)
res = 0
for i in range(len(input[0])):
    nums=[]
    for j in range(len(input)-1):
        nums.append(int(input[j][i]))
        
    if input[-1][i]=="*":
        res += math.prod(nums)
    else:
        res += sum(nums)

print(res)