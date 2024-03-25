#r=5
for i in range(1,6):
    for s in range(1,6-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("* ",end="")
    print()