
arr=list(map(int,input().split()))
n=int(input())
for i in range(0,len(arr),n):
    print(arr[i:i+n])
