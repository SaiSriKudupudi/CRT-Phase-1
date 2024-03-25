n=int(input("enter num:"))
s=0
for i in range(1,n):
    if n%i==0:
        s=s+i
print(s)
if s>n:
    print("greater than given number")
else:
    print("less than given number")