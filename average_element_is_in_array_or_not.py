n=int(input())
N=list(map(int,input().strip().split()))[:n]
s=0
for i in range(n):
    s+=i
avg=s/n
if avg in N:
    print("True")
else:
    print("False")