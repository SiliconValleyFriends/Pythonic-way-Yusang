import sys

sys.stdin=open("input.txt", "rt")

n, m = map(int, input().split())

ml = list(map(int, input().split()))

rt = ml[0]
lt = sum(ml)
max = max(ml)
res = lt

def Count(v):
    res = 1
    temp = 0
    for e in ml :
        if(temp + e <= v):
            temp += e
        else :
            temp = e
            res += 1
    return res
        
        

while rt<=lt:
    mid = (rt+lt) // 2
    if (max <= mid) and (Count(mid) <= m): #요구한 dvd 개수와 일치하거나 적다면
        res = mid
        lt = mid - 1
    else:
        rt = mid + 1

print(res)




        



