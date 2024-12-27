t=int(input())
for i in range (t):
    c=int(input())
    s1=input()
    s2=input()
    n=0
    for i in range (c):
        if (s1[i]=='G' and s2[i]=='R') or (s2[i]=='G' and s1[i]=='R') or (s1[i]=='B' and s2[i]=='R') or (s1[i]=='R' and s2[i]=='B'):
            n=1
            print('NO')
            break
    if n==0:
        print('YES')
