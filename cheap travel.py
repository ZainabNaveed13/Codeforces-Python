n,m,a,b=list(map(int,input().split()))
c4=999999999999999999999
c1=n*a
c2=((n//m)*b)+(((n-((n//m)*m)))*a)
c3=((n//m)*b)+(((n-((n//m)*m)))*b)
if m>n:
    c4=b
print(min(c1,c2,c3,c4))
