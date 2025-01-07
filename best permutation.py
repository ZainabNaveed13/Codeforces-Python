t=int(input())
for i in range (t):
    n=int(input())
    x=0
    m=1
    ran=1
    for i in range (n):
        ran=ran*m
        m+=1
    print(ran)
        
