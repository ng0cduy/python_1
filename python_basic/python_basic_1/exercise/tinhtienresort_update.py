tienphongloai1 = 1260000
tienphongloai2 = 1550000
tienphongloai3 = 1830000
tienphongloai4 = 1830000
tienphongloai5 = 2120000
tienphongloai6 = 2120000
tienphongloai7 = 2540000
tienphongloai8 = 4800000
# điều kiện cho loại phòng
try:
    loaiphong =int(input("Vui lòng nhập loại phòng với các mã\n(1) Standard\n(2) Superior Garden View\n(3) Superior Ocean View\n(4) Garden View Bugalow\n(5) Pool View Bugalow\n(6) Family Room\n(7) Beach Front Bugalow\n(8) VIP sea view\n"))
    assert(loaiphong>=1 and loaiphong <=8),'Vui lòng chỉ nhập từ 1 đến 8'
    sodem =int(input("Vui lòng nhập số đêm: "))
    assert(sodem >=1), 'Vui lòng nhập số đêm thích hợp (số đêm>0)'
except ValueError:
    print ("Vui lòng chỉ nhập số từ 1 đến 8")
except AssertionError as thongbao:
    print (thongbao)
else:
    if (loaiphong==1):
        tienphongMotDem=tienphongloai1
        tenphong='Standard'
    elif (loaiphong==2):
        tienphongMotDem=tienphongloai2
        tenphong='Superior Garden View'
    elif (loaiphong==3):
        tienphongMotDem=tienphongloai3
        tenphong='Superior Ocean View'
    elif (loaiphong==4):
        tienphongMotDem=tienphongloai4
        tenphong='Garden View Bungalow'
    elif (loaiphong==5):
        tienphongMotDem=tienphongloai5
        tenphong='Pool View Bungalow'
    elif (loaiphong==6):
        tienphongMotDem=tienphongloai6
        tenphong='Family Room'
    elif (loaiphong==7):
        tienphongMotDem=tienphongloai7
        tenphong='Beach Front Bungalow'
    elif (loaiphong==8):
        tienphongMotDem=tienphongloai8
        tenphong='VIP sea view'
    #tính tiền phòng
    if (sodem==1):
        tongtienphong=tienphongMotDem
    elif (sodem<=3):
        tongtienphong=tienphongMotDem*sodem*0.75
    else:
        tongtienphong=tienphongMotDem*sodem*0.7
    print (f'Loại phòng: {tenphong}')
    print (f'Số đêm ở: {sodem}')
    print (f'Tổng tiền phòng: {tongtienphong} VND')
