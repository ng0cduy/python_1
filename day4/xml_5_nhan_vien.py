from xml.dom.minidom import parse
class DonVi(object):
    '''
    classdoc: Don vi
    '''
    def __init__(self,iddvv,ten):
        self.iddv = iddvv
        self.ten = ten
class NhanVien(object):
    '''
    classdocs : Class Nhân viên
    '''
    def __init__(self,idnv,ho_ten,gioi_tinh,ngay_sinh,cmnd,muc_luong,dia_chi,iddv):
        '''
        constructor
        '''
        self.idnv = idnv
        self.ho_ten = ho_ten
        self.gioi_tinh = gioi_tinh
        self.ngay_sinh=ngay_sinh
        self.cmnd=cmnd
        self.muc_luong=muc_luong
        self.dia_chi=dia_chi
        self.iddv =iddv
    def in_thong_tin(self):
        gioi_tinh = ""
        if self.gioi_tinh == "True":
            gioi_tinh = "Nam"
        else:
            gioi_tinh = "Nữ"
        chuoi_kq = "ID nhân viên: " + self.idnv
        chuoi_kq+= "Họ tên: " + self.ho_ten
        chuoi_kq+= "Giới tính: " + gioi_tinh
        chuoi_kq+= "Ngày sinh: " + self.ngay_sinh
        chuoi_kq+= "CMND: " + self.cmnd
        chuoi_kq+= "Mức lương: " + self.muc_luong
        chuoi_kq+="Địa chỉ: " + self.dia_chi
        chuoi_kq+="ID đơn vị: "+self.iddv
        return chuoi_kq
def tao_danh_sach_don_vi(list_don_vi,link):
    tai_lieu = parse(link)
    node_root = tai_lieu.documentElement
    don_vi_s = node_root.getElementsByTagName("DON_VI")
    for don_vi in don_vi_s:
        if don_vi.hasAttribute("ID") and don_vi.hasAttribute("Ten"):
            dv = DonVi(don_vi.getAttribute("ID"),don_vi.getAttribute("Ten"))
            list_don_vi.append(dv)
    return list_don_vi
def tao_danh_sach_nhan_vien(list_nhan_vien,link):
    tai_lieu = parse(link)
    node_root = tai_lieu.documentElement
    nhan_vien_s = node_root.getElementsByTagName("NHAN_VIEN")
    for nhan_vien in nhan_vien_s:
        if nhan_vien.hasAttribute("ID") and nhan_vien.hasAttribute("Ho_ten"):
            nv =    NhanVien(nhan_vien.getAttribute("ID"),
                    nhan_vien.getAttribute("Ho_ten"),
                    nhan_vien.getAttribute("Gioi_tinh"),
                    nhan_vien.getAttribute("Ngay_sinh"),
                    nhan_vien.getAttribute("CMND"),
                    nhan_vien.getAttribute("Muc_luong"),
                    nhan_vien.getAttribute("Dia_chi"),
                    nhan_vien.getAttribute("ID_DON_VI"))
            list_nhan_vien.append(nv)
    return list_nhan_vien
def thong_ke_nhan_vien_theo_don_vi(iddv,ds_nhan_vien):
    tong_nv=0
    nv_nam=0
    nv_nu=0
    danh_sach_nhan_vien_theo_don_vi = []
    for item in ds_nhan_vien:
        if item.iddv == iddv:
            danh_sach_nhan_vien_theo_don_vi.append(item)
            tong_nv+=1
            if item.gioi_tinh == "true":
                nv_nam +=1
            else:
                nv_nu +=1
    return tong_nv,nv_nam,nv_nu,danh_sach_nhan_vien_theo_don_vi #tuple
def tim_kiem_nhan_vien(tu_khoa,ds_nhan_vien):
    ds_tim_kiem =[]
    for nv in ds_nhan_vien:
        if nv.ho_ten.lower().find(tu_khoa) != -1:
            ds_tim_kiem.append(nv)
    return ds_tim_kiem            
def in_danh_sach_nv(ds_nv):
    tieu_de = "DANH SÁCH NHÂN VIÊN ("+str(len(list_nhan_vien))+")"
    print (tieu_de.center(150))
    print("*"*151)
    print ( "ID".ljust(5),
                    "HỌ TÊN".ljust(30),
                    "Giới tính".ljust(10),
                    "Ngày sinh".ljust(15),
                    "CMND".ljust(10),"Mức lương".ljust(15),
                    "Địa chỉ".ljust(50),
                    "ID đơn vị".ljust(10))
    for item in ds_nv:
                # idnv,ho_ten,gioi_tinh,ngay_sinh,cmnd,muc_luong,dia_chi,iddv
        gt = "Nữ"
        if item.gioi_tinh=="true":
            gt="Nam"
        print ( item.idnv.ljust(5),
                item.ho_ten.ljust(30),
                gt.ljust(10),
                item.ngay_sinh.ljust(15),
                item.cmnd.ljust(10),
                item.muc_luong.ljust(15),
                item.dia_chi.ljust(50),
                item.iddv.ljust(10))
if __name__ == "__main__":
    lst_don_vi = []
    dv= tao_danh_sach_don_vi(lst_don_vi,"don_vi.xml")
    list_nhan_vien = []
    nv =tao_danh_sach_nhan_vien(list_nhan_vien,"nhan_vien.xml")
    while True:
        chuc_nang = int(input("\n Bạn muốn làm gì?\n1.In danh sách đơn vị\n2.In danh sách nhân viên\n3.Thống kê nhân viên theo đơn vị\n4. Tìm kiếm nhân viên\n=> "))
        if chuc_nang ==1:
            tieu_de = "DANH SÁCH ĐƠN VỊ ("+str(len(lst_don_vi))+")"
            print (tieu_de)
            print("*"*15)
            print ("ID".ljust(5),"Tên ĐV".ljust(10))
            for item in dv:
                print(item.iddv.ljust(5),item.ten.ljust(10))
        elif chuc_nang ==2:
            tieu_de = "DANH SÁCH NHÂN VIÊN ("+str(len(list_nhan_vien))+")"
            in_danh_sach_nv(nv)
        elif chuc_nang ==3:
            tieu_de = "DANH SÁCH ĐƠN VỊ ("+str(len(lst_don_vi))+")"
            print (tieu_de)
            print("*"*15)
            print ("ID".ljust(5),"Tên ĐV".ljust(10))
            for item in dv:
                print(item.iddv.ljust(5),item.ten.ljust(10))
            print("Thống kê nhân viên theo đơn vị:")
            donvi = int(input("Nhập đơn vị"))
            nv_theo_don_vi=thong_ke_nhan_vien_theo_don_vi(str(donvi),nv)[3]
            tong_nv = thong_ke_nhan_vien_theo_don_vi(str(donvi),nv)[0]
            nv_nam =thong_ke_nhan_vien_theo_don_vi(str(donvi),nv)[1]
            nv_nu = thong_ke_nhan_vien_theo_don_vi(str(donvi),nv)[2]
            in_danh_sach_nv(nv_theo_don_vi)
            print ("Tổng số nhân viên: ",tong_nv,"\nSố nv nam: ",nv_nam,"\nSố nv nữ: ",nv_nu)
        elif chuc_nang ==4:
            print("Tìm kiếm nhân viên")
            tu_khoa = input("Nhập họ tên cần tìm: ")
            ds_tim_kiem = tim_kiem_nhan_vien(tu_khoa,list_nhan_vien)
            in_danh_sach_nv(ds_tim_kiem)
        else:
            print ("\nChỉ được chọn 1,2,3,4")
        ans = input("Bạn có muốn tiếp tục nữa hay không?")
        if ans.lower() != 'y':
            break

