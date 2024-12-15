s=list(input())
count=0
for i in range (len(s)):
    if s[i]!=',' and s[i]!=' ' and s[i]!='{' and s[i]!='}' and s[i]!='-1':
        count+=1
        for j in range (i+1,len(s)):
            if s[i]==s[j]:
                s[j]='-1'
print(count)
            
