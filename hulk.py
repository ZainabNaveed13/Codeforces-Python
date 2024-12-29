def main():
    num=int(input())
    s=""
    for i in range (1,num+1):
        if i!=1:
            s+="that "
        if i%2!=0:
            s+="I hate "
        if i%2==0:
            s+="I love "
    s+="it"
    return s
print(main())
