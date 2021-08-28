from lib.class_TV import *
link = "database/ql_TV.db"
xl_TV = TV(link)
while True:
    chuc_nang =  int(input("Chọn chức năng\n1.Xem danh sách Tivi\n2.Thêm Tivi mới \
    \n3.Cập nhật Tivi\n4.Xóa Tivi\n5.Tìm Kiếm TV\n=>"))
    if chuc_nang == 1 :
        dsTV = xl_TV.doc_danh_sach_TV()
        print("DANH SÁCH SẢN PHẨM[",len(dsTV),"]")
        print("MÃ SỐ".ljust(15),"TÊN".ljust(50),"KÝ HIỆU".ljust(15),"ĐƠN GIÁ NHẬP".ljust(15),\
            "ĐƠN GIÁ BÁN".ljust(15),"SỐ LƯỢNG TỒN".ljust(15),"NHÓM TV".ljust(15))
        print("*"*150)
        for ds in dsTV:
            print (ds['Ma_so'].ljust(15),ds['Ten'].ljust(50),ds['Ky_hieu'].ljust(15),\
                    str(ds['Don_gia_Nhap']).ljust(15),str(ds['Don_gia_Ban']).ljust(15),\
                    str(ds['So_luong_Ton']).ljust(15),ds['Nhom_TV'].ljust(15))
    elif chuc_nang == 2 :
        ma_so = input("Nhập mã số: ")
        ten =input("Nhập tên: ")
        ky_hieu =  input("Nhập ký hiệu: ")
        don_gia_ban = int(input("Nhập đơn giá bán: "))
        don_gia_nhap = int (input("Nhập đơn giá nhập: "))
        so_luong_ton = int(input("Nhập số lượng tồn: "))
        nhom_TV = input("Nhập nhóm TV: ")
        kq = xl_TV.them_tivi(ma_so,ten,ky_hieu,don_gia_ban,don_gia_nhap,so_luong_ton,nhom_TV)
        if kq!= 0:
            print ("Cập nhật thành công!")
        else:
            print ("Cập nhật không thành công")
    elif chuc_nang == 3 :
        ds_ma_so = []
        for tivi in xl_TV.doc_danh_sach_TV():
            ds_ma_so.append(tivi['Ma_so'])
        ma_so = input("Nhập mã số: ")
        if ma_so in ds_ma_so:
            ten =input("Nhập tên: ")
            ky_hieu =  input("Nhập ký hiệu: ")
            don_gia_ban = int(input("Nhập đơn giá bán: "))
            don_gia_nhap = int (input("Nhập đơn giá nhập: "))
            so_luong_ton = int(input("Nhập số lượng tồn: "))
            nhom_TV = input("Nhập nhóm TV: ")
            kq = xl_TV.cap_nhat_tivi(ma_so,ten,ky_hieu,don_gia_ban,don_gia_nhap,so_luong_ton,nhom_TV)
            if kq!= 0:
                print ("Ghi thành công!")
            else:
                print ("Ghi không thành công")
        else:
            print("Mã số không tồn tại. Vui lòng thử lại.")
    elif chuc_nang == 4 :
        ds_ma_so = []
        for tivi in xl_TV.doc_danh_sach_TV():
            ds_ma_so.append(tivi['Ma_so'])
        ma_so = input("Nhập mã số: ")
        if ma_so in ds_ma_so:
            kq = xl_TV.xoa_TV(ma_so)
            if kq !=0:
                print("Xóa thành công")
            else:
                print ("Xóa không thành công")
        else:
            print("Không có dữ liệu để xóa,vui lòng thử lại")
    elif chuc_nang == 5 : 
        keyword = input("Nhập từ khóa: ")
        dsTV = xl_TV.tim_kiem(keyword)
        print("DANH SÁCH SẢN PHẨM ["+str(len(dsTV)).strip(" ")+"]")
        print("MÃ SỐ".ljust(15),"TÊN".ljust(50),"KÝ HIỆU".ljust(15),"ĐƠN GIÁ NHẬP".ljust(15),\
            "ĐƠN GIÁ BÁN".ljust(15),"SỐ LƯỢNG TỒN".ljust(15),"NHÓM TV".ljust(15))
        print("*"*150)
        for ds in dsTV:
            print (ds['Ma_so'].ljust(15),ds['Ten'].ljust(50),ds['Ky_hieu'].ljust(15),\
                    str(ds['Don_gia_Nhap']).ljust(15),str(ds['Don_gia_Ban']).ljust(15),\
                    str(ds['So_luong_Ton']).ljust(15),ds['Nhom_TV'].ljust(15))
    else:
        print("\nChỉ được chọn 1,2,3,4 hoặc 5")
    continue_ = input("Bạn có muốn tiếp tục nữa không? (y/n)\n =>").lower().strip()
    if continue_ == 'y':
        continue
    else:
        break
xl_TV.disconnect() 
    
    