import sys

# sys.stdin=open("input.txt", "rt")

l = list(map(int, input().split()))

o = {}

for i in range(1, l[0] + 1):
    for j in range(1, l[1] + 1):
        if i+j in o:
            o[i+j] += 1
        else:
            o[i+j] = 1

sl = sorted(o.items(), key= lambda x : x[1], reverse=True)

temp = sl[0][1]
for i in range(len(sl)):
    if(temp == sl[i][1]):
        print(sl[i][0], end = ' ')
    



        
