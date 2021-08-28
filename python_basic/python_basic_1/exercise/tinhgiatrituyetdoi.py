try:
    x=int(input("Nhập số nguyên x: "))
except ValueError:
    print ('Vui lòng nhập số nguyên')
else:
    if (x>=0):
        ketqua=x
    else:
        ketqua=x*(-1)
    print ("Giá trị tuyệt đối của số nguyên x = %d là |x| = %d" %(x,ketqua))