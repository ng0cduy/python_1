'''
Viết CT cho nhập vào số nguyên n.
Xử lý in ra màn hình n số nguyên được phát sinh ngẫu nhiên trong miền giá trị từ 10 đến 100
'''
import random
n = int (input("Input n: "))
i = 0
while (i<n):
    if (i<n-1):
        print (random.randint(10,100),end = ' , ')
    else:
        print (random.randint(10,100))
    i+=1
print ('Kết thúc')
