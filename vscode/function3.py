n=int(input("enter number="))
def check():
    a=n%10
    if a==5:
        return n**2
    elif a==3:
        return n**3
    elif a==6:
        return n-1
    else:
        return n/2
b=check()
print(b)

