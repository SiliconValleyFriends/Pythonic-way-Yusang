import sys

# sys.stdin=open("input.txt", "rt")


n = int(input())
l = list(input().split())


def reverse(x):
    t = list(x)
    t.reverse()
    return int(''.join(t))


def isPrime(x):
    if(x == 1) : return False
    if(x == 2): return True
    for i in range(2, x):
        if(x % i == 0):
            return False
    else :
        return True

for i in range(n):
    r = isPrime(reverse(l[i]))
    if (r):
        print(reverse(l[i]), end=' ')