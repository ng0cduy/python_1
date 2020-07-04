from thu_vien.class_DB import *
class NhomTivi(Database):
    def __init__(self,path_db):
        Database.__init__(self,path_db)

    def doc_danh_sach_nhom_tv(self):
        chuoi_sql = "SELECT * FROM NhomTiVi"
        noidung = Database.get_all(self,chuoi_sql)
        ds_nhom_TV = []
        for dong in noidung:
            nhom = {"Ma_so":dong[0],"Ten":dong[1]}
            ds_nhom_TV.append(nhom)
        return ds_nhom_TV
    def them_nhom_tivi(self,ma_so,ten):
        chuoi_sql = "INSERT INTO NhomTiVi VALUES(?,?)"
        kq=Database.execute(self,chuoi_sql,(ma_so,ten))
        return kq