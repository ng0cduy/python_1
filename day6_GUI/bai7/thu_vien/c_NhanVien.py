from thu_vien.class_DB import *
class NhanVien(Database):
    def __init__(self,path_db):
        Database.__init__(self,path_db)
    def doc_thong_tin_nhan_vien(self):
        chuoi_sql = "SELECT * FROM NhanVien"
        noidung = Database.get_all(self,chuoi_sql)
        ds_nhan_vien = []
        for dong in noidung:
            nhan_vien = {"ID":dong[0],"Ho_ten":dong[1],"Gioi_tinh":dong[2],"Ngay_sinh":dong[3],"CMND":dong[4],"Muc_luong":dong[5],"Dia_chi":dong[6],"ID_Don_Vi":dong[7]}
            ds_nhan_vien.append(nhan_vien)
            return ds_nhan_vien
    def them_nhan_vien(self,ma_so,ho_ten,ten_dang_nhap,mat_khau):
        chuoi_sql = "INSERT INTO NhanVien VALUES(?,?,?,?)"
        kq = Database.execute(self,chuoi_sql,(ma_so,ho_ten,ten_dang_nhap,mat_khau))
        return kq