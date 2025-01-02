t=int(input())
for i in range (t):
    s=list(map(int,input().split()))
    max1=0
    max2=0
    if s[0]>s[1]:
        max1=s[0]
        s[0]=0
    else:
        max1=s[1]
        s[1]=0
    if s[2]>s[3]:
        max2=s[2]
        s[2]=0
    else:
        max2=s[3]
        s[3]=0
    if (max2>s[0] and max2>s[1]) and (max1>s[2] and max1>s[3]):
        print('YES')
    else:
        print('NO')
        
