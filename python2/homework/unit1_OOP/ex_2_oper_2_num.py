class Operator(object):
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def addition(self):
        print ("Sum:",self.num1 + self.num2)
    def subtraction(self):
        print ("Difference:",self.num1 - self.num2 ) 
    def multiplication(self):
        print("Product:",self.num1 * self.num2)
    def division(self):
        print("Quotient: %.6f"%(self.num1 / self.num2))
if __name__ == "__main__":
    a = float (input("Input number a: "))     
    b = float (input("Input number b: "))         
    two_num_operator = Operator(a,b)
    two_num_operator.addition()
    two_num_operator.subtraction()
    two_num_operator.multiplication()
    two_num_operator.division()