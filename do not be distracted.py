t=int(input())
for i in range (t):
    num=int(input())
    n=input()
    l=[]
    for i in range (len(n)-1):
        if n[i]!=n[i+1]:
            l.append(n[i])
    if n[len(n)-1]!=n[len(n)-2]:
        l.append(n[len(n)-1])
    if len(l)==0:
        print('YES')
    else:
        a=0
        for i in range (len(l)):
            for j in range (i+1,len(l)):
                if l[i]==l[j]:
                    print('NO')
                    a=1
                    break
        if a==0:
            print('YES')
            
        
