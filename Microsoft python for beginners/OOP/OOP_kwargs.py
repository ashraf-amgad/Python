



class Car:
    def __init__(self, **kwargs):
        self.Data = kwargs
        print("class is initalized--------------------")
    
    def GetColor(self):
       print("the car color is : " + self.Data["color"]) 

    def GetOwner(self):
       print("the car owner is : " + self.Data["owner"])
    
    def GetModel(self):
       print("the car Model is : " + self.Data["model"])



AshrafCar = Car(owner="Ashraf Amgad", color="Red", model="BMW")
AshrafCar.GetColor()
AshrafCar.GetOwner()
AshrafCar.GetModel()

LoudaCar = Car(owner="Khaled Amgad", color="Black", model="KIA")
LoudaCar.GetColor()
LoudaCar.GetOwner()
LoudaCar.GetModel()

