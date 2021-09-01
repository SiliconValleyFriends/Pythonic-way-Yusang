import sys

# sys.stdin=open("input.txt", "rt")


n = int(input())
l = list(input().split())

max = sum(map(int,list(l[0])))
maxNum = l[0]

for i in range(1, n):
    r = sum(map(int,list(l[i])))
    if (max < r):
        max = r
        maxNum = l[i]

print(maxNum)
    
