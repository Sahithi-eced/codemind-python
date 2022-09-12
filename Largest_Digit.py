n = int(input())
sd = 9
ld = 0
while n > 0:
    r = n % 10
    if sd > r:
        sd = r
    if ld < r:
        ld = r
    n = int(n / 10)

print(ld)
