n = int(input('Nhập số nguyên n: '))
count = 0
if (n<=1):
    ketluan =f'Không có số nguyên nào nhỏ hơn {n}'
    print(ketluan)
else:
    ketluan =f'Các số nguyên tố nhỏ hơn {n} là: 2'
    print (ketluan,end = ' ')
    for i in range (3,n,1):
        for j in range (2,i,1):
            if(i%j==0):
               count=1
               break
            else: 
               count=0
        if count==0:
            print(i,end=' ')
print()
print('Kết thúc')