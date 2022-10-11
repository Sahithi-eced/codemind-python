n=int(input())
N=list(map(int,input().strip().split()))[:n]
a=int(input())
if a in N:
    print("True")
else:
    print("False")
