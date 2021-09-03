import sys

# sys.stdin=open("input.txt", "rt")


n = input()
res = []
count = 0

for i in range(len(n)):
    try:
        a = int(list(n)[i])
        res.append(str(a))
    except:
        0

res = int(''.join(res))

for j in range(1, int((res)/ 2 ) + 1):
    if(res / j - int(res /j) == 0):
        count += 1

print(res)
print(count + 1)