'''
	Viết chương trình cho phép nhập vào một chuỗi họ tên.
	Xử lý tách thành ba thành phần: Họ, Tên, Tên lót
'''
hoTen=input('Nhập họ tên: ')

hoTen=hoTen.strip()
i=hoTen.find(' ')
j=hoTen.rfind(' ')

ho=hoTen[0:i]
ten=hoTen[j+1:]
tenLot=hoTen[i+1:j]

print("Họ:",ho)
print("Tên lót:",tenLot)
print("Tên:",ten)

print('end')
