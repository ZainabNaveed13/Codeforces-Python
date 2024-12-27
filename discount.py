n=int(input())
a=list(map(int,input().split()))
m=int(input())
q=list(map(int,input().split()))
a.sort()
s=sum(a)
for i in range (m):
    print(s-a[len(a)-q[i]])
    
