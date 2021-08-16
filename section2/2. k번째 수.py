import sys


# sys.stdin=open("input.txt", "rt")


t = int(input())

for i in range(t):
    len, s,e,k = map(int, input().split())
    temp = input().split()
    temp = list(map(int, temp))
    
    slicedList = temp[s-1:e]
    slicedList.sort()
    
    print("#" + str(i+1) +" " + str(slicedList[k-1]))