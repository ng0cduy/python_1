import math
class Triangle():
    '''
    classdocs: Xay dung class xu ly ve tamgiac
    '''
    def __init__(self,_a_,_b_,_c_): #khong bao gio co return
        self.a= _a_
        self.b= _b_
        self.c= _c_
    def in_thong_tin_tam_giac(self): #k co tham so thi ghi self
        if (self.hop_le()==1):
            print ("\n3 canh cua tam giac la: " , self.a,self.b,self.c)
            print ("\nChu vi cua tam giac la: ",self.tinh_chu_vi())
            print ("\nDien tich la: ",self.tinh_dien_tich())
        else:
            print ("\n3 canh cua tam giac khong hop le!")
    def tinh_chu_vi(self):
        chuvi = self.a + self.b + self.c
        return chuvi
    def tinh_dien_tich(self):
        p_half=self.tinh_chu_vi()/2
        A= math.sqrt(p_half*(p_half-self.a)*(p_half-self.b)*(p_half-self.c)) 
        return A
    def hop_le(self):
        if (self.a+self.b > self.c and self.a+self.c>self.b and self.a+self.b >self.c):
            return 1
        else:
            return 0
    def __del__(self):
        pass
    
if __name__ =='__main__':
    # canh_1= float(input("\nNhap canh 1: "))
    # canh_2= float(input("\nNhap canh 2: "))
    # canh_3= float(input("\nNhap canh 3: "))
    # tamgiac1 = Triangle(canh_1,canh_2,canh_3)
    # tamgiac1.in_thong_tin_tam_giac()
    # tamgiac2 = Triangle(3,4,5)
    # tamgiac2.in_thong_tin_tam_giac()
    # print(getattr(tamgiac2,"b")) # gettor
    # print(hasattr(tamgiac2,"d")) #check for available
    # setattr(tamgiac2,"b",6) #settor
    # print(getattr(tamgiac2,"b")) # gettor
    print()