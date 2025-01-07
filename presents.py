n=int(input())
num=list(map(int,input().split()))
ans=[]
value=1
for i in range (len(num)):
    for j in range (len(num)):
        if num[j]==value:
            ans.append(j+1)
    value+=1
for i in range (len(ans)):
    print(ans[i],end=' ')

        

        
    
    
