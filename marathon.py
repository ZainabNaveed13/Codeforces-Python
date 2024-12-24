n=int(input())
for i in range (n):
    count=0
    v=list(map(int,input().split()))
    for j in range (1,len(v)):
        if v[j]>v[0]:
            count+=1
    print(count)
    
    
