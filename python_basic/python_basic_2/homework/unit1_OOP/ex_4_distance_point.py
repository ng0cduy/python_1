import math as m
class point(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distance_compute(self,B):
        distance = m.sqrt(pow((self.x-B.x),2) + pow((self.y-B.y),2))
        return distance
    # def print_distance(self):
    #     print ("Distance is :",distance_compute())
if __name__ == "__main__":
    aX = float (input("Input the x co-ordinate of point A: "))
    aY = float (input("Input the y co-ordinate of point A: "))
    A = point(aX,aY)
    bX = float (input("Input the x co-ordinate of point B: "))
    bY = float (input("Input the y co-ordinate of point B: "))
    B = point(bX,bY)
    print ("Distance between two point A(",aX,";",aY,")"," and B(",bX,",",bY,") is: ",B.distance_compute(A))
