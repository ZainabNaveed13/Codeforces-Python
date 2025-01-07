t=int(input())
for i in range (t):
    n=int(input())
    a=list(map(int,input().split()))
    min_diff=99999999999999999999999
    for j in range (len(a)):
        for k in range (j+1,len(a)):
            if abs(a[j]-a[k])<=min_diff:
                min_diff=abs(a[j]-a[k])
    print(min_diff)
        
