t=int(input())
for x in range (t):
    a,b=list(map(int,input().split()))
    moves=0
    if abs(abs(a)-abs(b))==0:
        moves=abs(a)+abs(b)
        print(moves)
    else:
        total=abs(a)+abs(b)
        diff=abs(abs(a)-abs(b))
        moves=(total-diff)+(2*diff)
        print(moves-1)
