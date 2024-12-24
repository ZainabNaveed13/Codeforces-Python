n,q=list(map(int,input().split()))
s=input()
for x in range (q):
    a,b=list(map(int,input().split()))
    count=0
    for i in range (a-1,b):
        count+=(ord(s[i])-96)
    print(count)
