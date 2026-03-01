
arr=list(map(int,input().split()))
seen=set()
dup=set()
for i in arr:
    if i in seen:
        dup.add(i)
    else:
        seen.add(i)
print(*dup)
