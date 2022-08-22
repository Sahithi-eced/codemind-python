n=int(input())
l=n
s=str(n)
c=0
t=n**2
x=''
u=str(t)
while(n>0):
    k=n%10
    c=c+1
    n=n//10
for i in range(c):
    d=t%10
    x=x+str(d)
    t=t//10
f=x[::-1]
if(f==s):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")