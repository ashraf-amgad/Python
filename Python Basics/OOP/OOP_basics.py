



class Car:
    def SetColor(self, color):
        self._Color = color

    def GetColor(self):
       print("the car color is : " + self._Color) 

    def SetOwner(self, owner):
        self._Owner = owner

    def GetOwner(self):
       print("the car owner is : " + self._Owner)




AshrafCar = Car()
AshrafCar.SetColor("Red")
AshrafCar.GetColor()

AshrafCar.SetOwner("Ashraf Amgad")
AshrafCar.GetOwner()


LoudaCar = Car()
LoudaCar.SetColor("Black")
LoudaCar.GetColor()

LoudaCar.SetOwner("Khaled Amgad")
LoudaCar.GetOwner()


