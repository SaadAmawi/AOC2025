with open("Day33.txt","r") as file:
    arr = list(battery for battery in file.read().split('\n'))

def part1(arr):
    res = []
    for line in arr:
        l = 0
        curr_max=0
        for r in range(1,len(line)):
            if l == r :
                continue
            if int(f"{line[l]}{line[r]}")>curr_max:
                curr_max=int(f"{line[l]}{line[r]}")
            if line[r]>line[l]:
                l = r
        res.append(curr_max)
    return res

def part2(arr):
    r=0
    for line in arr:
        numArr=[]
        max_deletions=len(line)-12
        for num in line:
            print(numArr)
            while(numArr and int(num)>numArr[-1] and max_deletions>0):
                    numArr.pop()
                    max_deletions-=1
                    print(numArr)
            numArr.append(int(num))
            print(numArr)
        while max_deletions>0:
            numArr=numArr[:len(numArr)-1]
            max_deletions-=1
        numArr=numArr[:12]
        output = (int(''.join(map(str,numArr))))
        print(output)
        r+=output
    return r
    
print(part2(arr))