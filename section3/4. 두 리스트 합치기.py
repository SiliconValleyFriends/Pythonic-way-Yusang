import sys

# sys.stdin=open("input.txt", "rt")

res = []

for i in range(2):
    n = input()
    l = map(int, input().split())
    res += l
res.sort()
print(' '.join(map(str, (res))))