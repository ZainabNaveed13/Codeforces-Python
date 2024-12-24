t = int(input())
for i in range (t):
    n = int(input())
    s=list(input())
    new = []
    new = set(s)
    if len(new)==7:
        print(6)
    else:
        print( 2**(len(new)-1))
   
