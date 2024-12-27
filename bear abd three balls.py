n=int(input())
t=list(map(int,input().split()))
ans=set(t)
a=[]
a+=ans
a=sorted(a, reverse=True)
m=0
for i in range (len(a)-2):
    if 0<a[i]-a[i+1]<=2 and 0<a[i]-a[i+2]<=2:
        print('Yes')
        m=1
        break
if m==0:
    print('No')
    
    
