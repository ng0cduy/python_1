from thu_vien.c_Database import *


class CongTy(Database):
    def __init__(self, path_db):
        Database.__init__(self, path_db)

    def doc_thong_tin_cong_ty(self):
        chuoi_sql = "SELECT * FROM CongTy"
        noi_dung = Database.get_all(self, chuoi_sql)
        ds_cong_ty = []
        for dong in noi_dung:
            cong_ty = {"Ten": dong[0], "Ma_so": dong[1], "Dien_thoai": dong[2], "Dia_chi": dong[3],
                       "Email": dong[4]}
            ds_cong_ty.append(cong_ty)
        return ds_cong_ty

    def cap_nhat_thong_tin_cong_ty(self, ten, ma_so, dien_thoai, dia_chi, email):
        chuoi_sql = "UPDATE CongTy SET Ten=?, Ma_so=?, Dien_thoai=?, Dia_chi=?, Email=?"
        kq = Database.execute(self, chuoi_sql, (ten, ma_so, dien_thoai, dia_chi, email))
        return kq

