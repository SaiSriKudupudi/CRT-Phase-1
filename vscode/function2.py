def login_system():
    # n=1
    # while n!=0:
    while True:
        un=(input("enter username:"))
        pw=(input("enter password:"))
        if un==pw:
            print("logged in")
            break
        else:
            print("enter correct details")
login_system()
