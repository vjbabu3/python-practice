
a=list(map(int,input().split()))
b=list(map(int,input().split()))
d=dict(zip(b,a))
print(*[d[i] for i in sorted(d)])
