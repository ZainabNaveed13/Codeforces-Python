n=int(input())
minn=0
maxx=0
x=n
n1=0
n2=0
while x!=0:
    if n1==0:
        if x>=5:
            x-=5
            n1=1
        else:
            x=0
            n1=1
    if n1==1:
        if x>=2:
            x-=2
            n1=0
            minn+=2
        else:
            minn+=x
            x=0
            n1=1
print(minn,end=' ')
while n!=0:
    if n2==0:
        if n>=2:
            maxx=maxx+2
            n=n-2
            n2=1
        else:
            maxx=maxx+n
            n=0
            n2=1
    if n2==1:
        if n>=5:
            n=n-5
            n2=0
        else:
            n=0
            n2=0
print(maxx)
            
