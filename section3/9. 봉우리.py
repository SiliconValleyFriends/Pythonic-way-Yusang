import sys

# sys.stdin=open("input.txt", "rt")

n = int(input())
l = [list(map(int,input().split())) for _ in range(n)]


count = 0


x = [0, 1, 0, -1]
y = [-1, 0, 1, 0]

for i in range(0, n):
    for j in range(0, n):
        for k in range(4):
            xi = j + x[k]
            yi = i + y[k]
            if xi < n and xi >= 0 and yi < n and yi >= 0:
                if l[yi][xi] >= l[i][j]:
                    break
        else:
            count += 1
            

        

print(count)
