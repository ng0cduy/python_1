from lib.class_DB import *

class TV(Database):
    def __init__(self, path_db):
        Database.__init__(self,path_db)
    def doc_danh_sach_TV(self):
        chuoi_sql = 'SELECT * FROM Tivi'
        noi_dung = Database.get_all(self,chuoi_sql)
        ds_TV = []
        for dong in noi_dung:
            tivi = {"Ma_so":dong[0],"Ten":dong[1],"Ky_hieu":dong[2],"Don_gia_ban":dong[3],"Don_gia_nhap":dong[4],\
                "So_luong_ton":dong[5],"Nhom_TV":dong[6]}
            ds_TV.append(tivi)
        return ds_TV