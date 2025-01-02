t=int(input())
for i in range (t):
    n=int(input())
    a=list(map(int,input().split()))
    ans=set(a)
    l=[]
    l+=ans
    count1=0
    count2=0
    for j in range (len(a)):
        if a[j]==l[0]:
            count1+=1
        if a[j]==l[1]:
            count2+=1
    if count1==1:
        for j in range (len(a)):
            if a[j]==l[0]:
                print(j+1)
                break
    if count2==1:
        for j in range (len(a)):
            if a[j]==l[1]:
                print(j+1)
                break
                
        
    
