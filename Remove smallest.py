t=int(input())
for x in range (t):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    count=0
    for i in range (len(a)-1):
        if abs(a[i]-a[i+1])==1:
            count+=1
        elif abs(a[i]-a[i+1])==0:
            count+=1
    if count==n-1:
        print('Yes')
    else:
        print('No')

