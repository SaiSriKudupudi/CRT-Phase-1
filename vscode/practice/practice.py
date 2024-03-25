for i in range(1,6):
    for s in range(1,i):
        print(" ",end=" ")
    for j in range(5,i-1,-1):
        print("*",end=" ")
    print()