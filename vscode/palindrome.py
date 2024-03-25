n=1221
n1=n
rev=0
while n>0:
    d=n%10
    n=n//10
    rev=rev*10+d
if rev==n1:
    print("palindrome")
else:
    print("not palindrome")