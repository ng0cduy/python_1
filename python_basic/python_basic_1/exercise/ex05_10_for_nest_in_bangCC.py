print ('*'*123)
print ('BẢNG CỬU CHƯƠNG'.center(123))
print ('*'*123)
for i in range (1,11):
    for j in range (2,10):
        ketqua = f'{j} x {i:2} = {j*i:2}'
        print(ketqua,end='\t')
    print ('\n')
print ('*'*123)
