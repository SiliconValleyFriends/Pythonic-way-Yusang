import sys

# sys.stdin=open("input.txt", "rt")

n, k = map(int, input().split())
l = list(map(int, input().split()))

p = []
for i in range(n-2):
    for j in range(i+1,n-1):
        for m in range(j+1, n):
            p.append(l[i]+l[j]+l[m])

p = list(set(p))
p.sort(reverse=True)




print(p[k-1])




