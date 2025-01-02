t=int(input())
for i in range (t):
    n=int(input())
    s=list(input())
    c=['T','i','m','u','r']
    if len(c)!=len(s):
        print('No')
    else:
        for j in range (len(c)):
            for k in range (len(c)):
                if c[j]==s[k]:
                    s[k]=-1
                    c[j]=-1
        ans=set(s)
        v=[]
        v+=ans
        if len(v)==1 and v[0]=='-1':
            print('Yes')
        else:
            print('No')
    
