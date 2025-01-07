t=int(input())
for i in range (t):
    n=int(input())
    s=list(input())
    maxx=ord(s[0])
    index=0
    for j in range (1,len(s)):
        if ord(s[j])<= maxx:
            index=j
            maxx=ord(s[j])
            ans=chr(maxx)
    new=''
    new+=ans
    for i in range (len(s)):
        if i!=index:
            new+=s[i]
    print(new)
            
            
            
    
    
