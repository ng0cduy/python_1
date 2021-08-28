import sqlite3

conn= sqlite3.connect('database/ql_nhan_vien.db')
print("Connect Successful")
chuoi_sql = "DELETE from NhanVien Where ID=?"
conn.execute(chuoi_sql,(8,))
conn.commit()
print ("Commit Successful")
conn.close()