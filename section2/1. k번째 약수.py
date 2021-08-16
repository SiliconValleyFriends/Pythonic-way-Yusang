import sys

#sys.stdin=open("input.txt", "rt")

n, k = map(int, input().split())

list = []

for i in range(1, n+1):
    if n % i  == 0 :
        list.append(i)
    if len(list) == k:
        print(list[k-1])
        break
else: #정상적으로 모두 끝나면
    print(-1)