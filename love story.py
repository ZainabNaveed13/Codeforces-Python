t=int(input())
for i in range (t):
    count=0
    s=input()
    c='codeforces'
    for j in range (len(c)):
        if s[j]!=c[j]:
            count+=1
    print(count)
