traloi = 'c'
while traloi.lower()== 'c':
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
    traloi=input('Bạn có muốn tiếp tục không[c|k]')
print ("Kết thúc")