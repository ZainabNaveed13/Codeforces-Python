n=int(input())
l=[]
for i in range (n):
    a=list(map(int,input()))
    for j in range (7):
        if a[j]==1:
            l.append(j+1)
num=[]
num+=set(l)
m=0
for i in range (len(num)):
    count=0
    for j in range (len(l)):
        if num[i]==l[j] and l[j]!=-1:
            count+=1
            l[j]=-1
        if j==len(l)-1 and count>=m:
            m=count
print(m)
            
            
    
    
                     
            
        
    
    
