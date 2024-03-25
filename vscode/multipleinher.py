class block:
    def blockname(self):
        print("main block")
class floor:
    def floorname(self):
        print("first floor")
class F15(block,floor):
    def roomname(self):
        print("room is f15")  
obj= F15()
obj.blockname()
obj.floorname()
obj.roomname()  