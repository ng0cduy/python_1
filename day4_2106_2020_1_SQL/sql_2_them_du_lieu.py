import sqlite3

conn = sqlite3.connect('database/ql_nhan_vien.db')
print("Successful")
#cách 1
# chuoi_sql = "INSERT INTO NhanVien (Ma_so,Ho_ten,CMND,SDT,Dia_chi) VALUES ('NV04','Nhân Viên 4','121212','09081231','Long An')"
# conn.execute(chuoi_sql)
# conn.commit()
# print("Successful")
# conn.close()
#CÁCH 2
# chuoi_sql = "INSERT INTO NhanVien (Ma_so,Ho_ten,CMND,SDT,Dia_chi) VALUES (?,?,?,?,?)"
# conn.execute(chuoi_sql,("NV05","Nhân viên 5","121212","090812312452","TPHCM"))
# conn.commit()
# print("Successful")
# conn.close()
#CÁCH 3
chuoi_sql = "INSERT INTO NhanVien VALUES (Null,?,?,?,?,?)"
conn.execute(chuoi_sql,("NV06","Nhân viên 6","151212","0912312452","TPHCM"))
conn.commit()
print("Successful")
conn.close()
