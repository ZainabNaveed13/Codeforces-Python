n=int(input())
m=int(input())
c=[]
for i in range (n):
    cap=int(input())
    c.append(cap)
c=sorted(c, reverse=True)
count=0
for i in range (len(c)):
    m=m-c[i]
    if m>0:
        count+=1
    if m<=0:
        count+=1
        print(count)
        break
   
        
