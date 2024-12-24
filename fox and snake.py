n,m=map(int,input().split())
x=1
for i in range (1,n+1):
    if i%2!=0:
        for j in range (m):
            print('#',end='')
        print()
    if i%2==0:
        for j in range (m):
            if x%2!=0:
                if j==m-1:
                    print('#')
                if j!=m-1:
                    print('.',end='')
            if x%2==0:
                if j==0:
                    print('#',end='')
                if j!=0 and j<m-1:
                    print('.',end='')
                if j==m-1:
                    print('.')
        x+=1
            
        
