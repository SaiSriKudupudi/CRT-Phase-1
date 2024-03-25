c=0
n=153
n1=n
n2=n
while n>0:
    n=n//10
    c=c+1
s=0
while n1>0:
    a=n1%10
    s=s+a**c
    n1=n1//10
print(s)
if s==n2:
    print("yes")
else:
    print("no")