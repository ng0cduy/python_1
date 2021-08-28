'''
    Viết chương trình xét tuyển sinh vào lớp 
    Nếu điểm >=5 thì gửi lời mời nhập học.
'''
hoTen = input('Nhập họ tên: ')
result = float(input("Nhập điểm: "))

if result >=5 and result <=10:
    ketqua = f'Chúc mừng bạn {hoTen} đã trúng tuyển!'
    print (ketqua)
else:
    print ('error')
print ('Kết thúc')