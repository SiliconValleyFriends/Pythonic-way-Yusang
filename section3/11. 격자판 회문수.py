import sys

# sys.stdin=open("input.txt", "rt")


l = [list(map(int,input().split())) for _ in range(7)]
count = 0

for i in range(3):
    for j in range(7):
        hor = l[j][i:i+5]
        if hor == hor[::-1]:
            count += 1

        ver = list(l[k][j] for k in range(i,i+5))
        if ver == ver[::-1]:
            count += 1

print(count)