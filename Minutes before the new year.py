t=int(input())
for i in range (t):
    h,m=list(map(int,input().split()))
    minutes=((23-h)*60)+(60-m)
    print(minutes)
