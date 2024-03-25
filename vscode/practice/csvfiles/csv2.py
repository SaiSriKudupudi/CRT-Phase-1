import csv
class LandR:
    def registration(self,username,password,phoneno,pincode,city):
        self.uname=username
        self.pwd=password
        self.pno=phoneno
        self.pin=pincode
        self.city=city
        with open("registration.csv","a",newline="") as file:
            store = csv.writer(file)
            store.writerow([self.uname,self.pwd,self.pno,self.pin,self.city])  
        #Resgistration done successfully
    def login(self,username,password):
        with open("registration.csv","r",newline="") as file:
            read = csv.DictReader(file)
            for row in read:
                if row["uname"] == username and row["pwd"] == password:
                    print("yes")
                else:
                    print("no")
        # return False

obj = LandR()
obj.registration("ram",123,1234,50019,"hyd")
obj.login("ram","1234")