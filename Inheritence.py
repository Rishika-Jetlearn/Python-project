class Electronics:
    def __init__(self,battery,colour,size,portable):
        self.power="off"
        self.battery=battery
        self.colour=colour
        self.size=size
        self.portable=portable
    def on(self):
        self.power="on"
        print("Turned on")
    def details(self):
        print(f"colour: {self.colour}")
        print(f"size: {self.size}")
device1=Electronics("yes","white","small","yes")
device1.on()
device1.details()
class Tv(Electronics):
    def __init__(self,battery,colour,size,portable,company):
        Electronics.__init__(self,battery,colour,size,portable)
        self.company=company
    def is_on(self):
        print(f"tv is {self.power}")


tv1=Tv("no","black","medium","no","Samsung")
tv1.details()
tv1.is_on()
tv1.on()
tv1.is_on()
device1.is_on()