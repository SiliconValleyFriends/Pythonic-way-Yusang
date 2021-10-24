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

while lt<=rt: #이 부분이 핵심
    mid = (lt+rt) // 2
    if Count(mid) >= m:
        res = mid
        lt = mid+1
    else:
        rt = mid-1
print(res)

#결정 알고리즘, 특정 범위내에 답이 있다는 것을 알때 사용한다.
#특정 중앙값이 답이 될 수 있는지를 함수를 통해 검사를 한 후 범위를 좁혀 나간다.

#N개의 랜선 길이가 lastest보다 클 수는 없기에 low =0, max = largest