t=int(input())
for i in range (t):
    a,b=map(int,input().split())
    count=(b-(a%b))%b
    print(count)
    
