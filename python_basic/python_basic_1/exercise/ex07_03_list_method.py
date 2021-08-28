# lstN=[1,3,5,7,9]
# # Thêm phần tử vào cuối danh sách
# lstN.append(11)
# # Chèn phần tử vào list tại vị trí chỉ định
# lstN.insert(2,11)

# # Đếm số lần xuất hiện của 1 giá trị phần tử|element|item trong list
# soLan=lstN.count(11)

# # Mở rộng list
# lstA=[1,2,3]
# lstB=[4,5,6,7]
# lstA.extend(lstB) # cộng giá trị vào địa chỉ cũ
# # lstA+=lstB


# Xác định| tìm vị trí của phần tử thỏa giá trị
# lst_N=[1,3,5,30,7,9,30,10]
# k1=lst_N.index(30) #--> 3
# k2=lst_N.index(30,k1+1) #--> 6
# j=lst_N.index(3) # Lỗi: ValueError (tìm không thấy)


# # Lấy 1 phần tử ra khỏi list
# lst_HoTen=['Lê','Thanh','Hải','Bình']
# ten=lst_HoTen.pop() # phần tử cuối
# ho=lst_HoTen.pop(0)

# # List --> str
# tenLot=' '.join(lst_HoTen)
# str_tenLot = ''.join(tenLot)
# lst_M=['12','14','15']
# str_M=','.join(lst_M)
# lst_SN=[10,20,30]
# strSN= str(lst_SN[])
# str_S='12,14,15'
# lst_S=str_S.split(',')

# # Xóa phần tử khỏi list khi biết giá trị
# lst_MaSo=['A01','A02','A03','A02']
# lst_MaSo.remove('A02')
# #lst_MaSo.remove('A02') #--> Lỗi ValueError

# # Xóa tất cả các phần tử trong list
# lst_MaSo.clear()
# # Xóa biến khỏi bộ nhớ
# del(lst_MaSo)


# # Sắp xếp
# lst_2=['an','binh','hoa','hue','bich','thu']
# lst_2.sort() # tăng
# lst_3=[2,3,1,4,6,5]
# lst_3.sort(reverse=True) # giảm

# # Đảo ngược giá trị các phần tử trong list
# lst_4=['a','b','c']
# lst_4.reverse()

# Demo phép gán của kiểu dữ liệu tham chiếu (reference type)
lst_2=[2,3,1,4,6,5]
lst_7=lst_2
lst_8=lst_2.copy()
lst_2.sort() # tăng
lst_7.append(5)
lst_2=[200,300]
# sorted : không làm ảnh huổng đến nội dung list gốc
print()
