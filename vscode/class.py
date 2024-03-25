class F15:
    def light(self):
        print("switching on the lights")
    def fan(self,speed):
        print("fan is on and the speed is",speed)
        self.s=speed
    def cpu(self):
        print("powering on the system")
        print(self.s)
student=F15()
student.light()
student.fan(5)
student.cpu()
