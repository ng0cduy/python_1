tienluong=5000 #-->int
hsl=1.275 #--> change from float to string
docThan=True #-->bool
hoten='Bùi Ngọc Duy' #-->str
thongTin1='Họ Tên: '+ hoten + '\nHệ số lương: ' +str(hsl) + '\nTiền lương: ' +str(tienluong)  
print (thongTin1)
thongTin2= ' Họ Tên: %s \n Hệ số lương: %.2f \n Tiền Lương: %i' %(hoten,hsl,tienluong)
print(thongTin2)