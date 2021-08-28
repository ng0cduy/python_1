'''
    Viết chương trình kiễm tra một số có phải là số nguyên tố hay không?
    Biết rằng: SNT là số tự nhiên khác 0, chỉ có 2 ước số dương phân biệt là 1 và chính nó. (1 không phải là SNT)
'''
n = int(input('Nhập số nguyên n: '))
if (n<=1):
    ketluan =f'{n} không phải là số nguyên tố'
else:
    ketluan =f'{n} là số nguyên tố'
    for i in range(2,n,1):
        if (n%i==0): 
            ketluan =f'{n} không phải là số nguyên tố'
            break
print ('Kết luận: ',ketluan)