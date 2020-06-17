import urllib.request,json
url =urllib.request.urlopen("http://lntpython.laptrinhpython.net:8181/dich-vu-san-pham/chi-tiet")
noidung = json.loads(url.read().decode())
stt =0
print ("STT".ljust(5),"TÊN SẢN PHẨM".ljust(30),"HÌNH SẢN PHẨM".ljust(50),"GÍA SIZE S".ljust(15),"GÍA SIZE M".ljust(15))
for i in noidung:
    stt+=1
    print (str(stt).ljust(5),i['ten_san_pham'].ljust(30),i['hinh_san_pham'].ljust(50),str(i['gia_size_s']).ljust(15),str(i['gia_size_m']).ljust(15))
