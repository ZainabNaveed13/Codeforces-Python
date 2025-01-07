t=int(input())
for x in range (t):
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    l=[]
    for i in range (len(a)):
        minn=0
        index=0
        diff=max(a)+1
        for j in range (len(b)):
            if abs(a[i]-b[i])<=k and abs(a[i]-b[i])<=diff:
                diff=abs(a[i]-b[i])
                minn=b[i]
                index=i
        l.append(minn)
        b[index]=max(b)+10
        print(b)
    print(l)
        
