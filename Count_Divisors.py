i,r,k=map(int,input().split())
s=0
for a in range(i,r+1):
    if a%k==0:
        s+=1
print(s)
    
