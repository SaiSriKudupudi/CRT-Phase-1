a=int(input("enter value"))
b=int(input("enter value"))
c=int(input("enter value"))
if a>80 and b>80 and c>80:
    print("A+")
elif ((a>60 and b>60 and c>60) and (a<80 and b<80 and c<80)):
    print("B+")
else:
    print("pass")
