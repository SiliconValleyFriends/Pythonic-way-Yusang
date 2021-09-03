import sys

# sys.stdin=open("input.txt", "rt")


l = [i for i in range(1, 21)]

for i in range(10) :
    s,e = map(int, input().split())
    l[s-1:e] = reversed(l[s-1:e])


print(' '.join(map(str, l)))

