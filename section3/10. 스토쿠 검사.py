import sys

# sys.stdin=open("input.txt", "rt")


l = [list(map(int,input().split())) for _ in range(9)]


for i in range(9):
    if len(list(set(l[i]))) != 9 :
        print('NO')
        break
    if len(list(set(list(l[k][i] for k in range(9))))) != 9:
        print('NO')
        break



else:
    print('YES')