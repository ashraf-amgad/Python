



class Car:
    def __init__(self, owner, color):
        self._Owner = owner
        self._Color = color
        print("class is initalized--------------------")
    
    def GetColor(self):
       print("the car color is : " + self._Color) 

    def GetOwner(self):
       print("the car owner is : " + self._Owner)



AshrafCar = Car("Ashraf Amgad" , "Red")
AshrafCar.GetColor()
AshrafCar.GetOwner()


LoudaCar = Car("Khaled Amgad", "Black")
LoudaCar.GetColor()
LoudaCar.GetOwner()


