n=int(input())
s=list(map(int,input().split()))
count_p=0
count_m=0
count_pe=0
for i in range (len(s)):
    if s[i]==1:
        count_p+=1
    elif s[i]==2:
        count_m+=1
    elif s[i]==3:
        count_pe+=1
minn=9999999999
if count_m<= count_p and count_m<=count_pe:
    minn=count_m
elif count_p<= count_m and count_p<=count_pe:
    minn=count_p
elif count_pe<=count_p and count_pe<=count_m:
    minn=count_pe
print(minn)
for i in range (minn):
    c1=0
    c2=0
    c3=0
    for j in range (len(s)):
        while s[i]!=1:
            if s[i]==1:
                print(c1+1,end=' ')
            else:
                c1+=1
        while s[i]!=2:
            if s[i]==2:
                print(c2+1,end=' ')
            else:
                c2+=1
        while s[i]!=3:
            if s[i]==3:
                print(c3+1)
            else:
                c3+=1
