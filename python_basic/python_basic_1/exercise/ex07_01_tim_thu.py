from datetime import datetime
try:
# 1- Nhập liệu & kiểm tra dữ liệu nhập
    strNgay=input('Nhập ngày (ngày/tháng/năm): ')
    btNgay=datetime.strptime(strNgay, '%d/%m/%Y')
except ValueError:
    print('Lỗi: nhập sai ngày sinh.')
else:
# 2- Xử lý tính toán
    thuTiengAnh=btNgay.strftime("%A")
    chiSoThu=btNgay.weekday()
    lst_Thu=['Thứ Hai','Thứ Ba','Thứ Tư','Thứ Năm','Thứ Sáu','Thứ Bảy','Chủ Nhật']
    thuTiengViet=lst_Thu[chiSoThu]
# 	if chiSoThu==0:
#    	    thuTiengViet='Thứ 2'
# 	elif chiSoThu==1:
#    	    thuTiengViet='Thứ 3'
# 	elif chiSoThu==2:
#    	    thuTiengViet='Thứ 4'
# 	elif chiSoThu==3:
#    	    thuTiengViet='Thứ 5'
# 	elif chiSoThu==4:
#    	    thuTiengViet='Thứ 6'
#     elif chiSoThu==5:
#         thuTiengViet='Thu 7'    
#     # else:
#     #     thuTiengViet='Chủ Nhật'
# print (thuTiengAnh)
# print (thuTiengViet)
