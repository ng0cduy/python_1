'''
giải phương trình tuyến tính ax+b=0
a=0
    b=0: vô số nghiệm
    nguoc lai: vô nghiệm
ngược lại:  1 nghiệm duy nhất -b/a
'''
print ("giải phương trình bậc nhất ax+b=0")
a= eval(input("Nhập tham số a: "))
b= eval(input("Nhập tham số b: "))
if a==0:
    if b ==0:
        ketqua = "có vô số nghiệm"
    else: 
        ketqua = "vô nghiệm"
else:
    nghiem=-b/a
    ketqua=f'có nghiệm duy nhất là {nghiem}'
# Output
ketqua_eqn = f'Phương trình {a}X + {b} = 0 {ketqua}'
print (ketqua_eqn)