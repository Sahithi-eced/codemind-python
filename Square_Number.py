def issquare(n):
    l=[]
    for i in range(n):
        l.append(i**2)
    for i in l:
        for j in l:
            if i+j==n:
                return True
    else:
        return False
n=int(input())
print(issquare(n))