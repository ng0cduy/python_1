while True:    
    try:
        loaixe = input('Loại xe (4 hoặc 7): ')
        assert(loaixe == '4' or loaixe == '7'),'>>> Lỗi: Nhập sai loại xe.'
        soKm   = float(input('Số km di chuyển: '))
        assert (soKm>0),'>>> Lỗi: Nhập sai số Km'
        thoiGianCho = int(input("Thời gian chờ: "))
        assert (thoiGianCho>0),'>>> Lỗi: Nhập sai thời gian chờ'
    except ValueError:
        print('>>> Lỗi: Nhập sai kiểu dữ liệu. Vui lòng nhập số')
    except AssertionError as thongbaoloi:
        print (thongbaoloi)
    else:
        #2.1 biện luận đơn giá theo loại taxi
        if loaixe =='4':
            DGmocua=11000
            DGtrong31=15300
            DGTren31=12100
        else: 
            DGmocua=12000
            DGtrong31=16100
            DGTren31=13800

        #2.2 Tính tiền di chuyển
        if soKm<=0.8:
            tiendichuyen=DGmocua
        elif soKm <=31:
            tiendichuyen= DGmocua+ DGtrong31*(soKm-0.8)
        else:
            tiendichuyen = DGmocua + DGtrong31*(31-0.8) + DGTren31*(soKm-31)

        tiencho = 0 if thoiGianCho<=5 else  (thoiGianCho-5) *750

        tongtienphaitra = tiencho + tiendichuyen
        print (f'Tiền chờ: {tiencho}')
        print (f'Tiền di chuyển:{tiendichuyen:,.2f}VND')
        print (f'Tiền cước:{tongtienphaitra:,.2f}VND')
    traloi = input ('Nhấn phím bất kì để tiếp tục. Để kết thúc nhấn phím [k]: ').lower()
    if traloi()=='k': break
print('Kết thúc')