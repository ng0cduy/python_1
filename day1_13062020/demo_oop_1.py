class XeOto():
    '''
    classdocs: Xay dung class xu ly ve xe oto
    '''
    mau_sac = "Đỏ"
    so_cho = 5
    doi_xe = 2018
    def in_thong_tin(self): #k co tham so thi ghi self
        print ("Mau sac: " + self.mau_sac + " \nSo cho ngoi: " + str(self.so_cho))

if __name__ =='__main__':
    oto_1= XeOto()
    oto_1.in_thong_tin()