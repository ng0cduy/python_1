import json
lst_SV = []
sv_1 = {"MSSV": "SV001","Họ tên":"Sinh viên 1","SDT":"090999999"}
sv_2 = {"MSSV": "SV002","Họ tên":"Sinh viên 2","SDT":"090999992"}
lst_SV = [sv_1,sv_2]
stt=0
while 1:
    stt+=1
    print ("Nhập thông tin cho sinh viên thứ ", stt)
    MSSV = input("Nhập Mã số sinh viên: ")
    Ho_ten = input ("Nhập họ tên: ")
    SDT = input("Nhập số điện thoại: ")
    sv = {"MSSV": MSSV,"Họ tên":Ho_ten,"SDT":SDT}
    lst_SV.append(sv)
    c = input("Bạn có muốn tiếp tục không? y/n: ")
    if c.lower() != "y":
        break
f =open("data/mssv.json",'w',encoding='utf-8')
json.dump(lst_SV,f,ensure_ascii=False,indent=4)
f.close()