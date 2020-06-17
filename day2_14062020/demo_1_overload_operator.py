class fraction(object):
    __a =100 #data hiding
    def __init__(self,num,denom):
        self.num = num
        self.denom = denom
    def __add__ (self,frac):
        new_num = self.num* frac.denom +self.denom* frac.num
        new_denom = self.denom * frac.denom
        return fraction(new_num,new_denom)
    def __sub__ (self,frac):
        new_num = self.num* frac.denom -self.denom* frac.num
        new_denom = self.denom * frac.denom
        return fraction(new_num,new_denom)
    def __mul__ (self,frac):
        new_num = self.num* frac.num
        new_denom = self.denom * frac.denom
        return fraction(new_num,new_denom)
    def __truediv__(self,frac):
        new_num = self.num* frac.denom
        new_denom = self.denom * frac.num
        return fraction(new_num,new_denom)
    def print_frac(self):
        print(self.num,"/",self.denom)
if __name__ == "__main__":
    
    frac1= fraction(2,3)
    frac2 = fraction(3,4)
    # frac1.addition(frac2).print_frac()
    (frac1/frac2).print_frac()
    print (frac1.__a)