from lib.class_DB import *
class DonVi(Database):
    def __init__(self,path_db):
        Database.__init__(self,path_db)
    def doc_danh_sach_don_vi(self):
        chuoi_sql = 'SELECT * FROM DonVi'
        noi_dung = Database.get_all(self,chuoi_sql)
        ds_DonVi = []
        for dong in noi_dung:
            Don_Vi = {"ID":dong[0],"Ten":dong[1]}
            ds_DonVi.append(DonVi)
        return ds_DonVi    