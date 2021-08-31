import sys
import math

# sys.stdin=open("input.txt", "rt")

n = int(input())
l = list(map(round, map(int, input().split())))
average = round( sum(l) / n)

num = 0
maxScore = l[0]

for i in range(1,n):
    if abs(average - l[i]) <= abs(average - maxScore):
        if abs(average - l[i]) == abs(average - maxScore):
            if l[i] > maxScore:
                num = i
                maxScore = l[i]
        elif abs(average - l[i]) < abs(average - maxScore):
            num = i
            maxScore = l[i]
            
        
        
            

            

print(str(average) + " " + str(num + 1))
        
        

