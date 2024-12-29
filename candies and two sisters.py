t=int(input())
for i in range (t):
    n=int(input())
    if n==2 or n==1:
        print('0')
    elif n%2==0:
        print((n//2)-1)
    else:
        print(n//2)
