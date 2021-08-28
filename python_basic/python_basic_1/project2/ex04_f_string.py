tienluong=5000 #-->int
hsl=1.273 #--> change from float to string
docThan=True #-->bool
hoten='Bùi Ngọc Duy' #-->str
thongTin1=f' Họ Tên: {hoten} \n Hệ số lương: {hsl:.2f} \n Tiền Lương: {tienluong}'
print(thongTin1)
print ('*'*50)
thongTin2=f' Họ Tên: {hoten} \n Hệ số lương: {round(hsl,2)} \n Tiền Lương: {tienluong}'
print(thongTin2)

#Literal String Interpolation
#f-string
#https://www.python.org/dev/peps/pep-0498/
