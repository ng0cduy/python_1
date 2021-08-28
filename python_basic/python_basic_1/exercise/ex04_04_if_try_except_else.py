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
except ValueError:
    print('>>> Lỗi: điểm phải nhập số')
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


