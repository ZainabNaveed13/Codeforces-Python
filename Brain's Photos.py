def main():
    n,m=map(int,input().split())
    c=[]
    s=0
    for i in range (n):
        a=list(input().split())
        for j in range (len(a)):
            c.append(a[j])
    for i in range (len(c)):
        if c[i]=='M' or c[i]=='C' or c[i]=='Y':
            s=1
            print('#Color')
            return
    if s==0:
        print('#Black&White')
main()
            
            

    
