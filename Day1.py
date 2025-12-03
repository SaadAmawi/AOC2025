with open("Day1.txt","r") as f:
    arr = list(line for line in f.read().split('\n'))

res = 0
i = 0
curr = 50
for combo in arr:
    direction = combo[0]
    rotation = int(combo[1::])

    if direction == "L":
        for i in range(rotation):
            curr-=1
            if curr == 0:
                res +=1
            if curr < 0:
                curr = 99
    else:
        for i in range(rotation):
            curr+=1
            if curr == 100:
                res += 1
                curr = 0

    

print(res)