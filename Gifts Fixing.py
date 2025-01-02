t=int(input())
for i in range (t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    min_a=min(a)
    min_b=min(b)
    max_a=max(a)
    max_b=max(b)
    moves=0
    while max_a!=min_a and max_b!=min_b:
        for i in range (len(a)):
            if a[i]>min_a and b[i]>min_b:
                moves+=1
                if a[i]==max_a:
                    max_a-=1
                if b[i]==max_b:
                    max_b-=1
                a[i]-=1
                b[i]-=1
            elif a[i]>min_a:
                moves+=1
                if a[i]==max_a:
                    max_a-=1
                a[i]-=1
            elif b[i]>min_b:
                moves+=1
                if b[i]==max_b:
                    max_b-=1
                b[i]-=1
    print(moves)
                

                    
                
        
        

        
    
        
                    
    
    
