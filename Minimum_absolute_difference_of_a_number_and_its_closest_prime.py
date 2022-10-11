n=int(input())
pp=n
np=n
while True:
    fc=0
    for i in range(1,np+1):
        if np%i==0:
            fc+=1
    if fc==2:
        break
    np+=1
while True:
    fc=0
    for j in range(1,pp+1):
        if pp%j==0:
            fc+=1
    if fc==2:
        break
    pp-=1
x=n-pp
y=np-n
if n-pp<=np-n:
    print(n-pp)
else:
    print(np-n)