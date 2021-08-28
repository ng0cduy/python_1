from lib.JSON_import import *
link= "data/mssv.json"
ds_sinh_vien = read_json_local(link)
while 1:
    print ("Nhập thông tin cho sinh viên")
    MSSV = input("Nhập Mã số sinh viên: ")
    Ho_ten = input ("Nhập họ tên: ")
    SDT = input("Nhập số điện thoại: ")
    sv = {"MSSV": MSSV,"Họ tên":Ho_ten,"SDT":SDT}
    ds_sinh_vien.append(sv)
    c = input("Bạn có muốn tiếp tục không? y/n: ")
    if c.lower() != "y":
        break 
kq = write_json_local(link,ds_sinh_vien)
if (kq==True):
    print("Ghi thành công")
else:
    print("That bai")
print(ds_sinh_vien)