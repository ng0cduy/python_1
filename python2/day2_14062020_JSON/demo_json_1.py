import json,urllib.request
f=open('du_lieu/QLCT_1.json', encoding ='utf-8')
content = json.load(f) # load: local files  loads: internet files
congty=content['CONG_TY'][0]
tencongty = congty['Ten']
donvi=content['DON_VI']
s=0
stt=0
#công ty
print('Tên công ty: ',tencongty)
print('Địa chỉ: ',congty['Dia_chi'])

# ĐƠN VỊ
for i in donvi:
    s += int(i['So_Nhan_vien'])
print('Tổng số nhân viên: ',s)
for i in donvi:
    stt+=1
    print (str(stt)," / ","Tên đơn vị: ",i['Ten'])
    print ("\t-Số nhân viên: ",int(i['So_Nhan_vien']))
    print ("\t-Tỷ lệ: ",i['Ty_le'],"%")