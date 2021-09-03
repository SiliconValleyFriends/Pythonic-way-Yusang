import sys

# sys.stdin=open("input.txt", "rt")


n = int(input())
for i in range(n):
    s = list(input().lower())
    if(''.join(s) == ''.join(reversed(s))):
        print('#' + str(i+1) + ' YES')
    else:
        print('#' + str(i+1) + ' NO')

