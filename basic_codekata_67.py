s=input()
v=[]
l=[]
n=''
for i in range(len(s)):
    if(i%2==0):
        v.append(s[i])
    else:
        l.append(s[i])
for j,k in zip(l,v):
    n=n+j+k
print(n)
