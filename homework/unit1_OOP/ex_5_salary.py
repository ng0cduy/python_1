class salary(object):
    def __init__(self,name,he_so_luong,luong_co_ban,so_nguoi_giam_tru_gia_canh,phu_cap):
        self.name = name
        self.he_so_luong = he_so_luong
        self.luong_co_ban = luong_co_ban
        self.so_nguoi_giam_tru_gia_canh = so_nguoi_giam_tru_gia_canh
        self.phu_cap = phu_cap
    def thu_nhap(self):
        return self.he_so_luong * self.luong_co_ban + self.phu_cap
    def thu_nhap_chiu_thue(self):
        return self.thu_nhap() - 9000000 -self.so_nguoi_giam_tru_gia_canh * 3600000
    def thue_TNCN(self):
        thue_TNCN = 0
        if self.thu_nhap_chiu_thue()/1000000 < 5:
            thue_TNCN = 0.05 * self.thu_nhap_chiu_thue()
            if thue_TNCN >= 250000:
                return 250000
            else:
                return thue_TNCN            
        elif self.thu_nhap_chiu_thue()/1000000 < 10:
            thue_TNCN = 0.1 * self.thu_nhap_chiu_thue()
            if thue_TNCN >= 500000:
                return 500000
            else:
                return thue_TNCN 
        elif self.thu_nhap_chiu_thue()/1000000 < 18:
            thue_TNCN = 0.15 * self.thu_nhap_chiu_thue()
            if thue_TNCN >= 1200000:
                return 1200000
            else:
                return thue_TNCN 
        elif self.thu_nhap_chiu_thue()/1000000 < 32:
            thue_TNCN = 0.2 * self.thu_nhap_chiu_thue()
            if thue_TNCN >= 2800000:
                return 2800000
            else:
                return thue_TNCN 
        elif self.thu_nhap_chiu_thue()/1000000 < 52:
            thue_TNCN = 0.25 * self.thu_nhap_chiu_thue()
            if thue_TNCN >= 5000000:
                return 5000000
            else:
                return thue_TNCN 
        else:
            thue_TNCN = 0.3 * self.thu_nhap_chiu_thue()
            if thue_TNCN >= 8400000:
                return 8400000
            else:
                return thue_TNCN 
    def thuc_linh (self):
        return self.thu_nhap() - self.thue_TNCN()
if __name__ == "__main__":
    name = input("Nhập tên: ")
    luong_index = float (input("Nhập hệ số lương: "))
    luong_co_ban = float (input("Nhập lương cơ bản: "))
    so_nguoi_giam = int(input("Nhập số người giảm trừ gia cảnh: "))
    phu_cap = float (input("Nhập phụ cấp: "))
    nv = salary(name,luong_index,luong_co_ban,so_nguoi_giam,phu_cap)
    print ("Thu nhập: ","{:,.0f}".format(nv.thu_nhap()))
    print ("Thu nhập chịu thuế: ","{:,.0f}".format(nv.thu_nhap_chiu_thue()))
    print ("Thuế TNCN: ","{:,.0f}".format(nv.thue_TNCN()))
    print ("Thực lĩnh: ","{:,.0f}".format((nv.thuc_linh())))
