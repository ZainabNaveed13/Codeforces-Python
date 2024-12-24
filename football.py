s=input()
count=1
for i in range (len(s)):
    if i!=len(s)-1 and s[i]==s[i+1]:
        count+=1
        if count==7:
            print('YES')
            break
    elif i!=len(s)-1 and s[i]!=s[i+1]:
        count=1
if count<7:
    print('NO')
