n=12467
c=0
while n>0:
    a=n%10
    n=n//10
    if a%2==0:
        c=c+1
print(c)