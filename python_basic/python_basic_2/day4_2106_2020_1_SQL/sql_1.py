import sqlite3

conn = sqlite3.connect('database/ql_nhan_vien.db')
print("Successful")

chuoi_sql = "SELECT Ma_so,Ho_ten,CMND,SDT,Dia_chi FROM NhanVien" # SELECT * FROM NhanVien
noidung = conn.execute(chuoi_sql)
for dong in noidung:
    print(dong)
conn.close()