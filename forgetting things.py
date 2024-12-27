a,b=list(map(int,input().split()))
count=1
if b-a==0:
    print(f'{a}{count} {b}{count+1}')
elif b-a==1:
    print(f'{a}{9} {b}{0}')
elif a==9 and b==1:
    print(f'{a} 10')
else:
    print(-1)
