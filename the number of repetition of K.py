a,k=input().split()
a=int(a)
k=int(k)
n=list(map(int,input().strip().split()))[:a]

print(n.count(k)-1)
