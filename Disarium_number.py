n=input()
s=int(n)
t=int(n)
sum=0
l=[]
c=0
for i in range(len(n)):
    r=s%10
    c+=1
    l.append(r)
    s=s//10
x=(l[::-1])
x.append(0)
for i in range(c):
    sum+=(int(x[i])**(i+1))
if sum==t:
    print("True")
else:
    print("False")