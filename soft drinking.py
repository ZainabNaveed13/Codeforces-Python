import math
n,k,l,c,d,p,nl,np=list(map(int,input().split()))
v1=math.floor(((k*l)/n)/n)
v2=math.floor((c*d)/n)
v3=math.floor((p/n)/n)
ans=min(v1,v2,v3)
print(int(ans))


