t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    c=0
    for j in range(a,b+1):
        s=str(j)
        if(s[-1]=="2") or (s[-1]=="3") or (s[-1]=="9"):
            c+=1
    print(c)