def is_prime():
    c=0
    n=int(input("enter number:")) 
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c==2:
        print("prime")
    else:
        print("not prime")
is_prime()