j= int(input("nhập số nguyên:"))
if (j>0 and j<10):
    print(f'Bảng cửu chương {j}')
    for i in range (1,11,1):
        print (f'{j} x {i:2} = {j*i:2}')
else:
    print ('nhập sai')
print('Kết thúc bảng cửu chương')