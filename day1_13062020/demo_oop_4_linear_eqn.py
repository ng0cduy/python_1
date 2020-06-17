class Linear_Eqn(object):
    '''
    classdocs: solving for linear equation
    '''
    def __init__(self,a,b):
        '''
        Constructor
        '''
        self.a = a
        self.b = b
    def solve_eqn(self):
        if (self.a ==0):
            if (self.b==0):
                output = "Infinite"
            else:
                output = "Can not solve"
        else:
            root = -self.b/self.a
            output = "Eqn have 1 root x= " + str(root)
        return output
    def print_solution(self):
        print (self.solve_eqn())
if __name__ == "__main__":
    print ("solving linear equation ax+b=0")
    a= float (input("Input a: "))
    b= float (input("Input b: "))
    eqn1 = Linear_Eqn(a,b)
    eqn1.print_solution()

