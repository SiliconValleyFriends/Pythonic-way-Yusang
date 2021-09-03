import sys

# sys.stdin=open("input.txt", "rt")

n, m = map(int, input().split())
l = list(map(int, input().split()))

count = 0

#index 2개
lt = 0
rt = 1

tot = l[0] #sum(l[lt:rt])


while(True):
    #현재 연산이 목표 값보다 작은 경우
    #오른쪽 포인터를 앞으로 이동시킨다.
    if tot < m:
        #오른족 포인터가 더 이상 갈 수 없다면 종료한다
        if rt == n:
            break
        tot += l[rt]
        rt += 1
    #현재 연산이 목표 값과 같은 경우
    #카운팅하고 왼쪽 포인터를 앞으로 이동시킨다.
    elif tot == m:
        count += 1
        tot -= l[lt]
        lt += 1
    #현재 연산이 목표 값보다 커진 경우
    #왼쪽 포인터를 앞으로 이동시킨다.
    elif tot > m:
        tot -= l[lt]
        lt += 1
    
        
print(count)
        

