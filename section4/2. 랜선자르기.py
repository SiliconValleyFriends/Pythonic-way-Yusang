import sys

# sys.stdin=open("input.txt", "rt")

def Count(len):
    cnt = 0
    for x in l :
        cnt+=(x//len)
    return cnt


n, m = map(int, input().split())

l = []
res = 0
largest = 0

for i in range(n):
    temp = int(input())
    l.append(temp)
    largest = max(largest, temp)

lt = 1
rt = largest

while lt<=rt:
    mid = (lt+rt) // 2
    if Count(mid) >= m:
        res = mid
        lt = mid+1
    else:
        rt = mid-1
print(res)
#