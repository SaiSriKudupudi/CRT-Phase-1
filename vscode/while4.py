s=0
n=47
n1=n
while n>0:
    a=n%10
    n=n//10
    s=s+a
print(s)
if n1%s!=0:
    print("not divisible")
else:
    print("divisible")