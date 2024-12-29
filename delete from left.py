s=list(input())
t=list(input())
moves=0
if len(s)==len(t):
    for i in range (len(s)):
        if s[i]!=t[i]:
            moves=(i+1)*2
    print(moves)
else:
    if len(s)>len(t):
        diff=len(s)-len(t)
        s=s[len(s)-len(t):]
        for i in range (len(s)):
            if s[i]!=t[i]:
                moves=(i+1)*2
        print(moves+diff)
    elif len(t)>len(s):
        diff=len(t)-len(s)
        t=t[len(t)-len(s):]
        for i in range (len(s)):
            if s[i]!=t[i]:
                moves=(i+1)*2
        print(moves+diff)
