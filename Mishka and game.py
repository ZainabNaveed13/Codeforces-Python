n=int(input())
count_m=0
count_c=0
draw=0
for i in range (n):
    m,c=list(map(int,input().split()))
    if m > c:
        count_m+=1
    elif c > m:
        count_c+=1
    elif  m == c:
        draw+=1
if count_m > count_c :
    print('Mishka')
elif count_c > count_m :
    print('Chris')
else :
    print('Friendship is magic!^^')
        
    
