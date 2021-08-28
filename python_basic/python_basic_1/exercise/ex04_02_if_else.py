'''
    Viết chương trình kết quả Đậu/Rớt
    đậu: dtb >=5, ngược lại là rớt
'''
diem = float(input("Nhập điểm trung bình: "))
if diem >=5:
    ketQua = "Đậu"
else:
    ketQua = "Rớt"
print ("Kết quả: ", ketQua)