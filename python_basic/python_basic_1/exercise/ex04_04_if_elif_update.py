'''
4.6 
    Xếp loại học sinh
    Quy ước xếp loại như sau:
    - ĐTB từ 8.0 trở lên - xếp loại "Giỏi"
    - ĐTB từ 6.5 trở lên - xếp loại "Khá"
    - ĐTB từ 5.0 trở lên - xếp loại "Trung Bình"
    - ĐTB từ 3.5 trở lên - xếp loại "Yếu"
    - ĐTB từ 0.0 trở lên - xếp loại "Kém"
'''
try:
    diem = float (input("Nhập điểm Tb: "))
    assert(diem>=0 and diem <=10),'>>> Lỗi: Điểm phải từ 0 tới 10'
except ValueError:
    print ("Lỗi: Điểm phải là số")
except AssertionError as Thongbaoloi:
    print(Thongbaoloi)
# except Exception as errMsg: # consider tất cả lỗi
#     print (errMsg)
else:
        if diem >=8:
            ketqua = "Giỏi"
        elif diem >=6.5:
            ketqua = "Khá"
        elif diem >=5:
            ketqua = "Trung bình"
        elif diem >3.5:
            ketqua = "Yếu"
        else:
            ketqua = "Kém"
        print ("kết quả xếp loại:", ketqua)
#********************************************************

# waittime = float (input("Nhập thời gian chờ theo phút: "))
# assert (sokm>=0 and waittime>=0),'>>> Vui lòng nhập số dương'