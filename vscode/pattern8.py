for i in range(1,5):
    for s in range(1,5-i):
        print("  ",end=" ")
    for j in range(1,2*i):
        if j==2*i or j==4 or i==4:
            print("* ",end=" ")
        else:
            print("  ",end=" ")
    print()