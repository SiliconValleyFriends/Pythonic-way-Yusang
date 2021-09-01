import sys

# sys.stdin=open("input.txt", "rt")


n = int(input())
l = list(map(int, input().split()))


ascore = 0
res = 0

for i in range(n):
    if l[i] == 0 :
        ascore = 0
    ascore += l[i]
    res += ascore

print(res)