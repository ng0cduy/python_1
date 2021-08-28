import sqlite3

conn= sqlite3.connect('database/ql_nhan_vien.db')
print("Connect Successful")

chuoi_sql = "UPDATE NhanVien SET Ma_so =?,Ho_ten=? WHere ID = ?"
conn.execute (chuoi_sql,("NV07","Nhân Viên 7",7))
conn.commit()
print("Commit Successful")
conn.close()