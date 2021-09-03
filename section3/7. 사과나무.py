import sys

# sys.stdin=open("input.txt", "rt")

n = int(input())
l = [list(map(int,input().split())) for _ in range(n)]

m = int(n / 2) 

res = 0

for i in range(n):
    if i <= m:
        res += sum(l[i][m-i : m+i+1])
    else:
        res += sum(l[i][i-m:n-(i-m) ])

print(res)

