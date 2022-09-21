n=int(input())
es=0
od=0
while n>0:
    r=n%10
    if r%2==0:
        es+=1
    else:
        od+=1
    n=n//10    
if od==0:
    print("Even")
elif es==0:
    print("Odd")
else:
    print("Mixed")
    