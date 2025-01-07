s=input()
p=0
n=len(s)
for i in range (len(s)):
    if s[i]=='o':
        p+=1
        n-=1
if p==0:
    print('Yes')
else:
    if n%p==0:
        print('Yes')
    else:
        print('No')
