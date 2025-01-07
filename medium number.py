t=int(input())
for i in range (t):
    num=list(map(int,input().split()))
    maxx=max(num)
    minn=min(num)
    for j in range (3):
        if num[j]!=maxx and num[j]!=minn:
            print(num[j])
            break
    
