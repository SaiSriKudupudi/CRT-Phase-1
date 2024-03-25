class carshowroom:
    def __init__(self):
        self.cgst=4000
        self.sgst=5000
        self.insurance=200000
    def company(self):
        while True:
            self.comname=input("enter the company name=")
            if self.comname=="toyota":
                print("welcome to toyota family")
                self.model()
                break
            elif self.comname=="mahindra":
                print("welcome to mahindra family")
                self.model()
                break
            elif self.comname=="mercedes":
                print("welcome to mercedes family")
                self.model()
                break
            else:
                print("enter valid companyname")
    def model(self):
        #while True:
        if self.comname=="toyota":
            while True:
                print("innova,fortuner")
                self.mod=input("enter model=")
                if self.mod=="innova":
                    self.price(self.mod)
                    break
                elif self.mod=="fortuner":
                    self.price(self.mod)
                    break
                else:
                    print("enter valid modal")
        elif self.comname=="mahindra":
            while True:
                print("scorpio,thar")
                self.mod=input("enter model=")
                if self.mod=="scorpio":
                    self.price(self.mod)
                    break
                elif self.mod=="thar":
                    self.price(self.mod)
                    break
                else:
                    print("enter valid modal")
        elif self.comname=="mercedes":
            while True:
                print("gwegan,amg")
                self.mod=input("enter model=")
                if self.mod=="gwegan":
                    self.price(self.mod)
                    break
                elif self.mod=="amg":
                    self.price(self.mod)
                    break
                else:
                    print("enter valid modal")
        else:
            print("enter valid companyname")
    def price(self,mod):
        if self.mod=="innova":
            self.price=1000000
        elif self.mod=="fortuner":
            self.price=3000000
        elif self.mod=="scorpio":
            self.price=2500000
        elif self.mod=="thar":
            self.price=1800000
        elif self.mod=="gwegan":
            self.price=10000000
        elif self.mod=="amg":
            self.price=5000000
        else:
            print("enter valid price")
        self.tot_price=self.price+self.sgst+self.cgst+self.insurance
        print(self.tot_price)
obj=carshowroom()
obj.company()
