def main():
    t=int(input())
    for i in range (t):
        n=int(input())
        a=list(map(int,input().split()))
        diff=1000
        for j in range (len(a)-1):
            if a[j+1]<a[j]:
                print('0')
                return
            if a[j+1]-a[j]<=diff:
                diff=a[j+1]-a[j]
        if diff==0:
            print('1')
        else:
            print(diff)
main()
            
        
        
    
