n=int(input())
s=0
p=1
while n>0:
        r=n%10
        s+=r
        if n>0:
            p*=r
            n=n//10
print(p-s)