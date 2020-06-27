import sqlite3
class Database(object):
    def __init__(self,path_db):
        self.conn = sqlite3.connect(path_db)

#Truy xuất DB
#Lấy Danh sách
    def get_all(self,chuoi_sql,btdk=()):
        cursor =self.conn.execute(chuoi_sql,btdk)
        danh_sach = cursor.fetchall()
        return danh_sach

#Lấy 1        
    def get_one(self,chuoi_sql,btdk=()):
        cursor =self.conn.execute(chuoi_sql,btdk)
        object_ = cursor.fetchone()
        return object_
#THỰC THI: INSERT,UPDATE,DELETE
    def execute(self,chuoi_sql,btdk=()):
        cursor = self.conn.execute(chuoi_sql,btdk)
        self.conn.commit()
        return cursor.rowcount
    def disconnect(self):
        self.conn.close()

