class block:
    def blockname(self):
        print("main block")
class floor(block):
    def floorname(self):
        print("first floor")
class F15(floor):
    def roomname(self):
        print("room is f15")  
obj= F15()
obj.blockname()
obj.floorname()
obj.roomname()  