from thu_vien.c_Database import *


class NhanVien(Database):
    def __init__(self, path_db):
        Database.__init__(self, path_db)

    def them_nhan_vien(self, ma_so, ho_ten, ten_dang_nhap, mat_khau):
        chuoi_sql = "INSERT INTO NhanVien VALUES (?, ?, ?, ?)"
        kq = Database.execute(self, chuoi_sql, (ma_so, ho_ten, ten_dang_nhap, mat_khau))
        return kq
