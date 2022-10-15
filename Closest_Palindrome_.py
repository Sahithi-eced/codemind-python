n=int(input())
l=[]
l1=[]
l2=[]
for i in range(11,n*3):
    s=str(i)
    s1=s[::-1]
    if s==s1:
        l.append(int(s1))
for j in l:
    if j<n:
        l1.append(j)
    elif j>n:
        l2.append(j)
a=n-l1[-1]
b=l2[0]-n
if a<b:
    print(l1[-1])
elif b<a:
    print(l2[0])
else:
    print(l1[-1],l2[0])