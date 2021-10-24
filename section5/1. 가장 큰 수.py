import sys

sys.stdin=open("input.txt", "r")

x , m = map(int, input().split())

stack = []
l = list(str(x))


for e in l :
    while len(stack)>0 and m > 0 and stack[-1]<e :
        stack.pop()
        m -= 1
    stack.append(e)

if m!= 0:
    stack = stack[:-m]

print("".join(stack))