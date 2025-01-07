n=int(input())
p=list(map(int,input().split()))
q=list(map(int,input().split()))
r=[]
num=1
for i in range (n):
    r.append(num)
    num+=1
t=[]
for i in range (len(p)):
    if i!=0:
        t.append(p[i])
for i in range (len(q)):
    if i!=0:
        t.append(q[i])
m=1
for i in range (len(r)):
    if r[i] not in t:
        print('Oh, my keyboard!')
        m=0
        break
if m==1:
    print('I become the guy.')
    
    
