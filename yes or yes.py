t=int(input())
for i in range (t):
    s=input()
    m=1
    if (s[0]=='Y' or s[0]=='y') and (s[1]=='E' or s[1]=='e') and (s[2]=='S' or s[2]=='s'):
        m=0
        print('YES')
    if m==1:
        print('NO')

            
