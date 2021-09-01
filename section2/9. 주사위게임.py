import sys

# sys.stdin=open("input.txt", "rt")


n = int(input())
res = -1

for i in range(n):
    t = list(map(int,input().split()))
    s = set(t)
    money = -1
    if len(s) == 1:
        money = 10000 + list(s)[0] * 1000
    elif len(s) == 2:
        if t[0] == t[1]:
            money = 1000 + t[0] * 100
        else :
            money = 1000 + t[2] * 100
    else:
        sort = sorted(t)
        money = sort[-1] * 100
    if res < money :
        res = money

print(res)



        


