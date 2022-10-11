n=int(input())
N=list(map(int,input().strip().split()))[:n]
sumofnum=0
count=0
for num in range(n):
    sumofnum+=num
    count+=1
avg=sumofnum/count
if avg in N:
    print("True")
else:
    print("False")