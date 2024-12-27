t=int(input())
for i in range (t):
    n=int(input())
    h=list(map(int,input().split()))
    b=list(map(int,input().split()))
    minn=999999999999999999
    sec=0
    for x in range (len(h)):
        for j in range (len(b)):
            if b[j]<=minn:
                minn=b[j]
                index=j        
        if index==0:
            sec+=h[index]
            h[index+1]+=minn
            b-=b[index]
            h-=h[index]
        elif index==len(h)-1:
            sec+=h[index]
            h[index-1]+=minn
            b-=b[index]
            h-=h[index]
        else:
            sec+=h[index]
            h[index+1]+=minn
            h[index-1]+=minn
            h-=h[index]
            b-=b[index]
    print(sec)
                
        
        
