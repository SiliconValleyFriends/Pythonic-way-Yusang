import sys

# sys.stdin=open("input.txt", "rt")

n = int(input())
l = [list(map(int,input().split())) for _ in range(n)]

m = int(input())

for i in range(m):
    r = list(map(int, input().split()))
    
    for j in range(r[2]):
        if r[1] == 0: #왼쪽으로 이동
            l[r[0]-1].append(l[r[0]-1].pop(0))
        else:

            l[r[0]-1].insert(0, l[r[0]-1].pop(-1))

res = 0

for j in range(n):
    if j <= int(n/2):
        res += sum(l[j][j:n-j])
    else:
        res += sum(l[j][n-1-j:j+1])

print(res)