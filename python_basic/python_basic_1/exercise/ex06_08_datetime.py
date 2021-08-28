# import datetime
# thoiDiemHienHanh=datetime.datetime.now()
#Cách 2:
# from datetime import datetime
from datetime import datetime,date
thoidiemhienhanh=datetime.now()
print(thoidiemhienhanh)
thoidiemhienhanh2=datetime.today()
print(thoidiemhienhanh2)
ngayHienHanh=date.today()
print(ngayHienHanh)

tpNgay=ngayHienHanh.day
tpThang=ngayHienHanh.month
tpNam=ngayHienHanh.year
 
# Khởi tạo biểu thức ngày 
ngaySinh1=datetime(2020,4,11)
    print(ngaySinh1)
ngaySinh2=date(2020,3,9)
print(ngaySinh2)
 
# Chuyển biểu thức ngày thành chuỗi thỏa theo mẫu định dạng
s1=ngayHienHanh.strftime("%d/%m/%y") #chuyển thành chuỗi
s2=ngayHienHanh.strftime("%d/%m/%Y")    #chuyển thành chuỗi
s3=ngayHienHanh.strftime("%A %d/%m/%Y") #chuyển thành chuỗi
thuTrongTuan=ngaySinh1.strftime("%A") # Full weekday name
print(thuTrongTuan) 
# Chuyển chuỗi thành biểu thức ngày
str_Ngay='25-3-2019'
bt_Ngay=datetime.strptime(str_Ngay,'%d-%m-%Y')

 
# chỉ số thứ trong tuần (0:Monday, 1:Tuesday,... 6: Sunday)
chiSoThu=bt_Ngay.weekday() #--> 0 
tenThuTA1=bt_Ngay.strftime("%A")  # Full weekday name
tenThuTA2=bt_Ngay.strftime("%a")  # Abbreviated weekday name
print(tenThuTA1,tenThuTA2) 
print()
 
# Format Code List
# https://www.programiz.com/python-programming/datetime/strftime
