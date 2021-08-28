n = int(input('Nhập số nguyên n: '))
if (n<=1):
    ketluan =f'{n} không phải là số nguyên tố'
else:
    
    for i in range(2,n,1):
        if (n%i==0): 
            ketluan =f'{n} không phải là số nguyên tố'
            break
    else: 
        ketluan =f'{n} là số nguyên tố'
print ('Kết luận: ',ketluan)