def is_prime():
    c=1
    n=int(input("enter number:")) 
    for i in range(2,n):
        if n%i==0:
            c=0
            break
    if c==0:
        print("not prime")
    else:
        print("prime")
is_prime()