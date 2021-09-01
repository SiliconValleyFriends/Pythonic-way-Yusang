import sys

# sys.stdin=open("input.txt", "rt")


n = int(input())
count = 0

for i in range(1, n):
    for j in range(2, int(i / 2 )):
        if(i / j == 0):
            break;
    else:
        count += 1

print(count)