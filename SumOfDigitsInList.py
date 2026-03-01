
arr=list(map(int,input().split()))
print(*[sum(map(int,str(abs(i)))) for i in arr])
