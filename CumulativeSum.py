
arr=list(map(int,input().split()))
s=0
res=[]
for i in arr:
    s+=i
    res.append(s)
print(*res)
