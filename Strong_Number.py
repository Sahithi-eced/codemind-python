sum1=0
num=int(input())
temp=num
while(num):
    i=1
    f=1
    r=num%10
    while(i<=r):
        f=f*i
        i=i+1
    sum1=sum1+f
    num=num//10
if(sum1==temp):
    print("The number %d is a strong number"%sum1)
else:
    print("The number %d is not a strong number"%temp)