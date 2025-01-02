def main():
    t=int(input())
    for i in range (t):
        m=1
        s=list(input())
        if len(s)%2!=0:
            print('NO')
        else:
            s1=[]
            for j in range (len(s)//2,len(s)):
                s1.append(s[j])
            for j in range (0,len(s)//2):
                if s1[j]!=s[j]:
                    print('NO')
                    m=0
                    break
            if m==1:
                print('YES')
main()
            
        
            
