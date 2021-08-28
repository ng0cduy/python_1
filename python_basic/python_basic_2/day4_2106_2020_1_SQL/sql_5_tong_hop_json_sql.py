from lib.JSON_import import *
import os
import sqlite3
conn =sqlite3.connect('database/ql_TV.db')
print('Kết nối thành công')
duong_dan_thu_muc_TV = "database/Tivi"
for tap_tin in os.listdir(duong_dan_thu_muc_TV):
    noi_dung = read_json_local(duong_dan_thu_muc_TV + "/"+tap_tin)

    #gán biến
    ma_so = noi_dung["Ma_so"]
    ten = noi_dung["Ten"]
    ky_hieu = noi_dung["Ky_hieu"]
    don_gia_ban = noi_dung["Don_gia_Ban"]
    don_gia_nhap = noi_dung["Don_gia_Nhap"]
    so_luong_ton = noi_dung["So_luong_Ton"]
    nhom_TV = noi_dung["Nhom_Tivi"]["Ma_so"]

    #khai bao cau lenh truy van
    chuoi_sql = "INSERT INTO Tivi values (?,?,?,?,?,?,?)"
    conn.execute(chuoi_sql,(ma_so,ten,ky_hieu,don_gia_ban,don_gia_nhap,so_luong_ton,nhom_TV))
    conn.commit()
    print("Done"+ma_so)
conn.close()