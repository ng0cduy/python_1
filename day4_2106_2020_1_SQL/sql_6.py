from lib.JSON_import import *
import sqlite3
from xml.dom.minidom import parse
conn= sqlite3.connect('database/DonVi.db')

#Đơn vị
# duong_dan_file_don_vi = parse("database/don_vi.xml")
# node_root = duong_dan_file_don_vi.documentElement
# don_vi_s = node_root.getElementsByTagName("DON_VI")
# for don_vi in don_vi_s:
#     _id = don_vi.getAttribute('ID')
#     ten = don_vi.getAttribute('Ten')
#     print (_id,ten)
#     #dua DL vào DB
#     chuoi_sql = 'INSERT INTO DonVi Values (?,?)'
#     conn.execute(chuoi_sql,(_id,ten))
#     conn.commit()

#nhân viên
duong_dan_file_nhan_vien = parse("database/nhan_vien.xml")
node_root = duong_dan_file_nhan_vien.documentElement
nhan_vien_s = don_vi_s = node_root.getElementsByTagName("NHAN_VIEN")
for nhan_vien in nhan_vien_s:
    _id = nhan_vien.getAttribute('ID')
    ho_ten = nhan_vien.getAttribute('Ho_ten')
    gt = nhan_vien.getAttribute('Gioi_tinh')
    ngay_sinh = nhan_vien.getAttribute('Ngay_sinh')
    cmnd = nhan_vien.getAttribute('CMND')
    muc_luong = nhan_vien.getAttribute('Muc_luong')
    dia_chi = nhan_vien.getAttribute('Dia_chi')
    ID_don_vi = nhan_vien.getAttribute('ID_DON_VI')
    print (ho_ten)
    #dua data vào DB
    chuoi_sql = "INSERT INTO NhanVien VALUES (?,?,?,?,?,?,?,?)"
    conn.execute(chuoi_sql,(_id,ho_ten,gt,ngay_sinh,cmnd,muc_luong,dia_chi,ID_don_vi))
    conn.commit()
conn.close()
