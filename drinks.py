n=int(input())
p=list(map(int,input().split()))
s=0
for i in range(len(p)):
    s+=p[i]
ans=s/len(p)
print(ans)
