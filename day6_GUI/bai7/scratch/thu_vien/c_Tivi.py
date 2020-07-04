from thu_vien.c_Database import *

class Tivi(Database):
    def __init__(self, path_db):
        Database.__init__(self, path_db)

    def them_tivi(self, ma_so, ten, ki_hieu, don_gia_ban, don_gia_nhap, so_luong_ton, nhom_tivi):
        chuoi_sql = "INSERT INTO Tivi VALUES (?, ?, ?, ?, ?, ?, ?)"
        kq = Database.execute(self, chuoi_sql, (ma_so, ten, ki_hieu, don_gia_ban, don_gia_nhap, so_luong_ton, nhom_tivi))
        return kq

