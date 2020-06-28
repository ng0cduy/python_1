from lib.class_DB import *

class TV(Database):
    def __init__(self, path_db):
        Database.__init__(self,path_db)
    def doc_danh_sach_TV(self):
        chuoi_sql = 'SELECT * FROM Tivi'
        noi_dung = Database.get_all(self,chuoi_sql)
        ds_TV = []
        for dong in noi_dung:
            tivi = {"Ma_so":dong[0],"Ten":dong[1],"Ky_hieu":dong[2],"Don_gia_Ban":dong[3],"Don_gia_Nhap":dong[4],\
                "So_luong_Ton":dong[5],"Nhom_TV":dong[6]}
            ds_TV.append(tivi)
        return ds_TV
    def them_tivi (self,ma_so,ten,ky_hieu,don_gia_ban,don_gia_nhap,so_luong_ton,nhom_tv):
        chuoi_sql = "INSERT INTO Tivi Values (?,?,?,?,?,?,?)"
        kq = Database.execute(self,chuoi_sql,(ma_so,ten,ky_hieu,don_gia_ban,don_gia_nhap,so_luong_ton,nhom_tv))
        return kq
    def cap_nhat_tivi(self,ma_so,ten,ky_hieu,don_gia_ban,don_gia_nhap,so_luong_ton,nhom_tv):
        chuoi_sql = "UPDATE Tivi SET Ten =?,Ky_hieu=?,Don_gia_Ban =?,Don_gia_Nhap=?,\
                    So_luong_Ton =?,Nhom_Tivi=? WHere Ma_so = ?"
        kq =Database.execute(self,chuoi_sql,(ten,ky_hieu,don_gia_ban,don_gia_nhap,so_luong_ton,nhom_tv,ma_so))
        return kq
    def xoa_TV(self,ma_so):
        chuoi_sql = "DELETE FROM Tivi where Ma_so=?"
        kq=Database.execute(self,chuoi_sql,(ma_so,))
        return kq
    def tim_kiem (self,keyword):
        chuoi_dk = "%" + keyword + "%"
        chuoi_sql = 'SELECT * FROM Tivi Where Ten like ?'
        noi_dung = Database.get_all(self,chuoi_sql,(chuoi_dk,))
        ds_TV = []
        for dong in noi_dung:
            tivi = {"Ma_so":dong[0],"Ten":dong[1],"Ky_hieu":dong[2],"Don_gia_Ban":dong[3],"Don_gia_Nhap":dong[4],\
                "So_luong_Ton":dong[5],"Nhom_TV":dong[6]}
            ds_TV.append(tivi)
        return ds_TV
