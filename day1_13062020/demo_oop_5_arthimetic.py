class arthimetic_2_nums(object):
    '''
    classdocs: solving for linear equation
    '''
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 =num2
    def addition(self):
        return (self.num1 + self.num2)
    def subtraction (self):
        return (self.num1 - self.num2)
    def multiplication (self):
        return (self.num1 * self.num2)
    def division (self):
        return (self.num1 / self.num2)
    def power(self):
        return pow(self.num1,self.num2)
if __name__ == "__main__":
    num1= float(input("Input number 1: "))
    num2= float(input("Input number 2: "))
    arr1 = arthimetic_2_nums(num1,num2)
    print(arr1.addition())
    print(arr1.subtraction())
    print(arr1.multiplication())
    print(arr1.division())
    print(arr1.power())
