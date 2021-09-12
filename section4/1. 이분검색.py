import sys

# sys.stdin=open("input.txt", "rt")

n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

high = n
low = 0
mid = -1


while True:
    mid = int((high+low) / 2)
    if arr[mid] == m:
        print(mid+1)
        break
    elif arr[mid] < m:
        low = mid+1
    elif arr[mid] > m:
        high = mid-1
