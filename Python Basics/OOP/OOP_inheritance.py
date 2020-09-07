



class Sum_Sub:
    def Sum(self, number_1 , number_2):
        print("summition is ", str(number_1 + number_2))
    
    def Sub(self, number_1 , number_2):
       print("Subtraction is ", str(number_1 - number_2)) 




class Calculator(Sum_Sub):
    def Mult(self, number_1 , number_2):
        print("Multiplication is ", str(number_1 * number_2))
    
    def Div(self, number_1 , number_2):
       print("Division is ", str(number_1 / number_2)) 




calc = Calculator()

calc.Sum(12 , 2)
calc.Sub(12 , 2)
calc.Mult(12 , 2)
calc.Div(12 , 2)


