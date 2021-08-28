import math
class Polygon(object):
    def __init__(self,num_of_sides):
        self.num_of_sides =num_of_sides
        self.sides = []
    def input_sides(self):
        for i in range (0,self.num_of_sides):
            self.sides.append(float(input("Input side "+str(i+1)+ ": ")))
    def display_sides(self):
        for i in range (0,self.num_of_sides):
            print ("Side " + str(i+1) + " : " + str(self.sides[i]))
class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)
    def perimeter (self):
        a,b,c = self.sides
        p =a+b+c
        return p
    def area(self):
        a,b,c = self.sides
        p1=self.perimeter()/2
        A = math.sqrt(p1*(p1-a)*(p1-b)*(p1-c))
        return A
    def valid(self):
        a,b,c=self.sides
        if (a+b>c and a+c>b and b+c>a):
            return 1
        else:
            return 0
    def __del__ (self):
        pass
class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,2) #super: inheritance from base class
    def perimeter (self):
        a,b = self.sides
        p = (a+b)*2
        return p
    def area (self):
        a,b = self.sides
        Area = a*b
        return Area
    def __del__ (self):
        pass
if __name__ ==  "__main__":
    while True:
        function = int(input("Choose shape to print information: \n1.Triangle\n2.Rectangle\n=>"))
        if function ==1:
            tri1= Triangle()
            tri1.input_sides()
            if tri1.valid() == True:
                tri1.display_sides()
                print ("P= ", tri1.perimeter())
                print ("A= ", tri1.area())
            else:
                print("Invalid")
            print (isinstance(tri1,Triangle))
        elif function ==2:
            rec1 = Rectangle()
            rec1.input_sides()
            rec1.display_sides()
            print ("P= ", rec1.perimeter())
            print ("A= ", rec1.area())
        else:
            print("Please only choose 1 or 2")
        continue_ = input("Do you want to continue? (y/n)\n=>")
        if (continue_.lower() == 'y'):
            continue
        else:
            break