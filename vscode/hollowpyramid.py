#hollow pyramid
for i in range(1,5):
    for j in range(1,5-i):
        print("  ",end=" ")
    for j in range(1,2*i):
        if j==1 or j==2*i-1 or i==4:
            print("* ",end=" ")
        else:
            print("  ",end=" ")
    print()
#reverse hollow pyramid
for i in range(1,5):
    for s in range(1,i):
        print("  ",end=" ")
    for j in range(1,(4*2-(2*i-1))+1):
        if j==1 or j==4*2-(2*i-1) or i==1:
            print("* ",end=" ")
        else:
            print("  ",end=" ")
    print()
