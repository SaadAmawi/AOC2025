from collections import deque

with open("Day4.txt","r") as f:
    arr = list([l for l in line] for line in f.read().split('\n'))

r = len(arr)
c = len(arr[0])


directions = [(1,0),(0,1),(1,1),(-1,0),(0,-1),(-1,-1),(1,-1),(-1,1)]


def findRemovable(arr):
    res=0
    removable = []
    for x in range(r):
        for y in range(c):
            if arr[x][y]=="@":
                count=0
                for dx,dy in directions:
                    cx,cy=x+dx,y+dy
                    if 0<=cx<r and 0<=cy<c:
                        if arr[cx][cy]=="@":
                            count+=1
                if count < 4:
                    res+=1
                    removable.append((x,y))
    return removable

def final(arr):
    count=0
    while True:
        remove = findRemovable(arr)
        if not remove:
            return count
        count+=len(remove)
        for x,y in remove:
            arr[x][y]="."
        
print(final(arr))
