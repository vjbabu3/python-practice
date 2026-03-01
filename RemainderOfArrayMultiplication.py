
n=int(input())
arr=list(map(int,input().split()))
mod=int(input())
res=1
for i in arr:
    res=(res*i)%mod
print(res)
