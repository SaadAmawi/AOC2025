with open("Day2.txt","r") as f:
    nums = [
        [str(n) for n in range(int(a), int(b) + 1)]
        for a, b in (s.split("-") for s in f.read().split(","))
    ]

res = 0

def isInvalid(num):
    divisors = []
    l = len(num)

    for i in range(1,len(num)):
        if len(num)%i==0:
            divisors.append(i)
            
    for div in divisors:
        st = num[:div]*(l//div)
        if st == num:
            return True

for arr in nums:
    for num in arr:
        if isInvalid(num):
            res+=int(num)

print(res)