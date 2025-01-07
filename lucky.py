n=int(input())
for i in range (n):
    s=input()
    sum1=0
    for i in range (0,3):
        num1=int(s[i])
        sum1+=num1
    sum2=0
    for j in range (3,6):
        num2=int(s[j])
        sum2+=num2
    if sum2==sum1:
        print('Yes')
    else:
        print('No')
        
        
