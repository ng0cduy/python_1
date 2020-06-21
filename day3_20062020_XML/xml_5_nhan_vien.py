from xml.dom.minidom import parse
class DonVi(object):
    '''
    classdoc: Don vi
    '''
    def __init__(self,iddvv,ten):
        self.iddv = iddvv
        self.ten = ten
class NhanVien(object):
    '''
    classdocs : Class Nhân viên
    '''
    def __init__(self,idnv,ho_ten,gioi_tinh,ngay_sinh,cmnd,muc_luong,dia_chi,iddv):
        '''
        constructor
        '''
        self.idnv = idnv
        self.ho_ten = ho_ten
        self.gioi_tinh = gioi_tinh
        self.ngay_sinh=ngay_sinh
        self.cmnd=cmnd
        self.muc_luong=muc_luong
        self.dia_chi=dia_chi
        self.iddv =iddv
    def in_thong_tin(self):
        gioi_tinh = ""
        if self.gioi_tinh == "True":
            gioi_tinh = "Nam"
        else:
            gioi_tinh = "Nữ"
        chuoi_kq = "ID nhân viên: " + self.iddv
        chuoi_kq+= "Họ tên: " + self.ho_ten
        chuoi_kq+= "Giới tính: " + gioi_tinh
        chuoi_kq+= "Ngày sinh: " + self.ngay_sinh
        chuoi_kq+= "CMND: " + self.cmnd
        chuoi_kq+= "Mức lương: " + self.muc_luong
        chuoi_kq+="Địa chỉ: " + self.dia_chi
        chuoi_kq+="ID đơn vị: "+self.iddv
        return chuoi_kq