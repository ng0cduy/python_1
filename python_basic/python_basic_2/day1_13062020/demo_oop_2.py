class XeOto():
    '''
    classdocs: Xay dung class xu ly ve xe oto
    '''
    mau_sac = "Đỏ"
    so_cho = 5
    doi_xe = 2018
    def in_thong_tin(self,mau_sac,so_cho,doi_xe): #k co tham so thi ghi self
        print ("Mau sac: " + mau_sac + " \nSo cho ngoi: " + str(so_cho))

if __name__ =='__main__':
    oto_1= XeOto()
    oto_1.in_thong_tin("Xanh",7,2020)