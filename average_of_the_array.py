n=int(input())
N=list(map(int,input().strip().split()))[:n]
sumofnum=0
count=0
for num in N:
    sumofnum+=num
    count+=1
avg=sumofnum/count
a="{:.2f}".format(avg)
print(a)