# # Khởi tạo list

# lst_R1=[]
# lst_R2=list()

# lst_N=[200,10,30,100]
# lst_Thu=['Thứ Hai','Thứ Ba','Thứ Tư','Thứ Năm','Thứ Sáu','Thứ Bảy','Chủ Nhật']
# lst_K=['001','Trần văn An',True,1.5,500]

# # In nội dung list ra màn hình
# print(lst_Thu)

# # Tổng số phần tử trong list
# tongSoPT=len(lst_Thu) # --> 7
# # Tổng giá trị các phần tử trong list lst_N
# tongGT=sum(lst_N)
# # Tìm min
# giaTriNN=min(lst_N)
# # Tìm min
# giaTriLN=max(lst_N)

# # # Truy xuất giá trị của phần tử trong list khi biết chỉ số index
# gtPT_dauTien=lst_Thu[0]
# gtPT_cuoi1=lst_Thu[-1]

# i=len(lst_Thu)-1 # chỉ số index của phần tử cuối cùng trong list
# gtPT_cuoi2=lst_Thu[i]

# # Gán lại|thay đổi giá trị của phần tử thứ 2 trong lst_N với giá trị mới là 50
# lst_N[1]=50

# # Xóa phần tử trong list
# lst_ThuTV=['Thứ Hai','Thứ Ba','Thứ Tư','Thứ Năm','Thứ Sáu','Thứ Bảy','Chủ Nhật']
# # Xóa 1 phần tử trong list khi biết chỉ số index
# del(lst_ThuTV[2]) # xóa 'Thứ Tư'
# # Xóa nhiều phần tử trong list
# del(lst_ThuTV[1:4]) # start: 1, stop: 4 (xóa từ 1 đến 3)

# # Ghép|Cộng dữ liệu các list
lst_N1=[1,3,5]
lst_N2=[2,4,6,8]
lst_N3=lst_N1 + lst_N2

# # Đúp| Nhân dữ liệu của list lên nhiều lần
# lst_N4=lst_N1*4

# # Rút trích dữ liệu trong list
# lst_ThuTV=['Thứ Hai','Thứ Ba','Thứ Tư','Thứ Năm','Thứ Sáu','Thứ Bảy','Chủ Nhật']
# lst_NgayLamViec=lst_ThuTV[0:5]  # start:0, stop:5  (lấy từ 0 đến 4)
# lst_NgayNghi=lst_ThuTV[5:] # start:5 (Từ 5 lấy hết phần còn lại)
# # Kiểm tra một giá trị có tồn tại trong list không
# k1= 4 in lst_N2
# k2= 4 in lst_N1
# k3= 'Thứ Ba' in lst_NgayLamViec

# giaTri='Thứ Tư'
# k4 = giaTri in lst_NgayNghi
print()
