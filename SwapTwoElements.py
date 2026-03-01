
arr=list(map(int,input().split()))
i,j=map(int,input().split())
arr[i],arr[j]=arr[j],arr[i]
print(*arr)
