n,m=list(map(int,input().split()))
if n==m:
    print('0')
elif m==0:
    print('1')
elif n%2==0:
    print((n//m)-1)
elif n%2!=0 and m%2==0:
    print(n%m)
else:
    print((n//m)+1)
