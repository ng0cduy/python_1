import urllib.request,json
import csvgit
url =urllib.request.urlopen("http://lntpython.laptrinhpython.net:8181/dich-vu-san-pham/chi-tiet")
noidung = json.loads(url.read().decode())
stt =0
print (("DANH SÁCH SẢN PHẨM ("+str(len(noidung))+ ")").center(5+30+50+30))
print ("STT".ljust(5),"TÊN SẢN PHẨM".ljust(30),"HÌNH SẢN PHẨM".ljust(50),"GIÁ SIZE S".ljust(15),"GIÁ SIZE M".ljust(15))
print ("-"*(5+30+50+30))
list_sp =[]
for i in noidung:
    stt+=1
    print (str(stt).ljust(5),i['ten_san_pham'].ljust(30),i['hinh_san_pham'].ljust(50),"{:,}".format(i['gia_size_s']).ljust(15),"{:,}".format(i['gia_size_m']).ljust(15))

    sp= [i['ten_san_pham'],i['hinh_san_pham'],i['gia_size_s'],i['gia_size_m']]
    list_sp.append(sp)
   
f = open('data/dssp.csv','w',encoding='utf-8',newline='')
for item in list_sp:
    csv.writer(f).writerow(item)
f.close()