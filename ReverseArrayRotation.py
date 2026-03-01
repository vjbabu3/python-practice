
n=int(input())
arr=list(map(int,input().split()))
k=int(input())
k%=n
arr=arr[::-1]
arr=arr[k:]+arr[:k]
print(*arr[::-1])
