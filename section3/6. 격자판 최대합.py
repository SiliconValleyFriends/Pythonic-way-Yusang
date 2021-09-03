import sys

# sys.stdin=open("input.txt", "rt")

n = int(input())
l = [list(map(int,input().split())) for _ in range(n)]

largest = - 2147000000

for i in range(n):
    horizental = vertical = 0
    for j in range(n):
        horizental += l[i][j]
        vertical += l[j][i]
    if horizental > largest :
        largest = horizental
    if vertical > largest :
        largest = vertical

#대각선
ltrb = rtlb = 0
for i in range(n):
    ltrb += l[i][i]
    rtlb += l[i][n-i-1]
if ltrb > largest :
        largest = ltrb
if rtlb > largest :
        largest = rtlb

print(largest)