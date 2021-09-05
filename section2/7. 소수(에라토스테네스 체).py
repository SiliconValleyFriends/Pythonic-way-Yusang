import sys

# sys.stdin=open("input.txt", "rt")

n = int(input())
l = list(0 for _ in range(n+1))
count = 0

for i in range(2, n+1):
    if l[i] == 0:
        count += 1
        for j in range(int(n/i)+1):
            l[j*i] = 1

print(count)