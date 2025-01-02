n=int(input())
a=list(map(int,input().split()))
ans=sum(a)/n
if ans>=4.5:
    print('0')
count=0
if ans<4.5:
    while ans<4.5:
        minn=5
        index=0
        for i in range (len(a)):
            if a[i] < minn:
                minn=a[i]
                index=i
        count+=1
        a[index]=5
        ans=(sum(a))/n
    print(count)
    
            
