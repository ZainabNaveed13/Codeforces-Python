t=int(input())
for x in range (t):
    n=int(input())
    a=list(map(int,input().split()))
    maxx=0
    count=0
    for i in range (len(a)):
        if i!=len(a)-1 and a[i]==0:
            count+=1
        elif i!=len(a)-1 and a[i]!=0:
            if count>=maxx:
                maxx=count
                count=0
        elif i==len(a)-1:
            if a[i]==0:
                count+=1
                if count>=maxx:
                    maxx=count
                    print(maxx)
                else:
                    print(maxx)
            else:
                print(maxx)
                
