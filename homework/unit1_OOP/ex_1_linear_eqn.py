class Linear_Eqn(object):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def solving (self):
        if self.a ==0:
            if self.b ==0:
                output = "Infinite solutions"
            else:
                output = "No solution"
        else:
            output = -self.b/self.a
        return output
    def print_solution(self):
        print ("Result: ",self.solving())

if __name__ == "__main__":
    a= float (input("Input number for a: "))
    b= float (input("Input number for b: "))
    eqn1 = Linear_Eqn(a,b)
    eqn1.print_solution()