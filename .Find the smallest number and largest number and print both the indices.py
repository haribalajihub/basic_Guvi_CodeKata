n=int(input())
a=list(map(int,input().strip().split()))
x=min(a)
y=max(a)
b=a.index(x)
c=a.index(y)
print(int(b)+1,int(c)+1)
