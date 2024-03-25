class shopping:
    def dresstype(self,dt):
        # print("the dresstype is",dt)
        self.d=dt
    def price(self,pr):
        # print("the dress price is",pr)
        self.p=pr
    def size(self,sz):
        # print("the dress size",sz)
        self.s=sz
    def display(self):
        print(self.d)
        print(self.p)
        print(self.s)
function = shopping()
function.dresstype("kurti")
function.price(500)
function.size(40)
function.display()
