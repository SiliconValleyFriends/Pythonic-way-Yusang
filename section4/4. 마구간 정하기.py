import sys

sys.stdin=open("input.txt", "r")

n, c=map(int, input().split())

l=[]
for _ in range(n):
    l.append(int(input()))

l.sort()

lt = 1
rt = max(l) - min(l)
res = 0

def Count(v):
    h = 1 #말의 개수
    current = l[0]
    for e in l[1:] :
        if e - current >= v :
            h += 1
            current = e
    return h
#값보다 모든 말의 거리가 같거나 커야함.


while lt <= rt :
    mid = (lt+rt) // 2
    if Count(mid) >= c: #이곳에는 요구하는 특정 개수가 와야함
        lt = mid + 1
        res = mid
    else : 
        rt = mid - 1

print(res)
            
