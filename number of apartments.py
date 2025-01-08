t=int(input())
for x in range (t):
    n=int(input())
    if n%3==0:
        print(f'{x//3} 0 0')
    elif n%5==0:
        print(f'0 {x//5} 0')
    elif n%7==0:
        print(f'0 0 {x//7}')
    
