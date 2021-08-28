# s1='trung tÂm tin học   '
# k1=s1.capitalize()  # --> 'Trung tâm tin học   '
# k2=s1.upper() #--> 'TRUNG TÂM TIN HỌC   '
# k3=s1.lower() #--> 'trung tâm tin học   '
# k4=s1.title() #--> 'Trung Tâm Tin Học   '
 
# k5=s1.strip() #--> 'trung t m tin học'
# s2=',20,30,'
# k6=s2.strip(',') #--> '20,30'
 
# s3='Xin chào "Hùng"!'
# print(s3)
 
# s4="Xin chào \"Hùng\"!"
# print(s4)
 
 
 
# baiTho="""
# Thánh thót tàu tiêu mấy hạt mưa,
# Khen ai khéo vẽ cảnh tiêu sơ.
# Xanh om cổ thụ tròn xoe tán,
# Trắng xoá trường giang phẳng lặng tờ.
 
# Bầu dốc giang sơn, say chấp rượu,
# Túi lưng phong nguyệt, nặng vì thơ.
# Cho hay cảnh cũng ưa người nhỉ,
# Thấy cảnh ai mà chẳng ngẩn ngơ.
# """
 
# tieuDe1=" Tức cảnh chiều thu ".center(37,"*")
# tieuDe2=" Tức cảnh chiều thu ".center(37)
# print("*"*37)
# print(tieuDe1)
# print(tieuDe2)
# print("*"*37)
# print(baiTho)
 
# k7=baiTho.count('cảnh') #đếm trong bài thơ có bao nhiêu chữ 'cảnh', phân biệt chữ hoa và chữ thường
# k8=baiTho.count('cảnh',0,100) # đếm trong các kí tự từ kí tự start tới kí tự stop
 
# tongSoKyTu=len('thánh thót')
# d1='thánh thót'.count('t',0,10) #--> 3
# d2='thánh thót'.count('t',1,10) #--> 2
 
# k9=baiTho.find('cảnh') #-> 50
# k10=baiTho.find('Cảnh') # Tìm không thấy: -1
 
# hoTen="Trần Lê Anh Thư"
# i=hoTen.find(' ') # 4 #vi trí khoảng trắng đầu tiên từ trái qua
# j=hoTen.rfind(' ') # 11 #vi trí khoảng trắng đầu tiên từ phải qua
# Ten1=hoTen[j+1:]
# Ten2=hoTen[j:].lstrip()
# Ho1 =hoTen[:i].rstrip()
# middle_name = hoTen[i+1:j]
# s5="123456"
# kq1=s5.isdigit() #--> True 
# s6="abc"
# s7="123vnd"
# s8="12320"
# s9='ASD'
# kq2=s6.isalpha()
# kq3=s7.isalpha()
# kq4=s8.isnumeric()
# kq5=s6.islower()
# kq6=s9.isupper()
 
# print()
 
# soTien=12000000.453
# str_SoTien1='{:,}VND'.format(soTien)    # '12,000,000.453VND'
# str_SoTien2='{:,.2f}VND'.format(soTien) # '12,000,000.45VND'
# # str_SoTien=str_SoTien1.replace(',','.')
 
# str_SoTien3='{:15}'.format(soTien)  # '   12000000.453'
# str_SoTien4='{:<15}'.format(soTien) # '12000000.453   '
 
# # f-string (v3.6)
# tienDiChuyen=56000.475
# str_SoTien5=f'Tiền di chuyển: {tienDiChuyen:,}VNĐ'      # 'Tiền di chuyển: 56,000.475VNĐ'
# str_SoTien6=f'Tiền di chuyển: {tienDiChuyen:,.1f}VNĐ'   # 'Tiền di chuyển: 56,000.5VNĐ'
# str_SoTien7=f'{tienDiChuyen:15}'  # '      56000.475'
# str_SoTien8=f'{tienDiChuyen:<15}' # '56000.475      '
 
 
# str1=str_SoTien1.rjust(20,'*') # '***12,000,000.453VND'
# str2=str_SoTien1.ljust(20,'*') # '12,000,000.453VND***'
 
# str3=str_SoTien1.rjust(20) # '   12,000,000.453VND'
# str4=str_SoTien1.ljust(20) # '12,000,000.453VND   '
# str5=str_SoTien1.center(21) # ' 12,000,000.453VND  '
# str6=str(tienDiChuyen).ljust(20) # '56000.475      
hoten ="Họ và tên"
stt = "STT"
sotien="Số tiền"
import random
str_test= f'{stt:5}|{hoten.center(40):40}|{sotien.center(20):20}|' 
print (str_test) 
for i in range(1,5,1):
    str_test1 =f'{i:5}|{"abc".center(40):40}|{"abc".center(20):20}|'
    print (str_test1)
 
