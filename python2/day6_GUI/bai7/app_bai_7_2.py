from giao_dien.gd_Bai_7_2 import *
from thu_vien.c_Nhom_Tivi import *
from thu_vien.xu_ly_chung import *
xl_nhom_tivi = NhomTivi(duong_dan_tivi)
ds_nhom_tivi= xl_nhom_tivi.doc_danh_sach_nhom_tv()
print (ds_nhom_tivi)
ds_ten_nhom_tivi = []

for nhom_tivi in ds_nhom_tivi:
    ds_ten_nhom_tivi.append(nhom_tivi['Ten'])
# Khởi tạo đối tượng nhóm TIVI
app = wx.App()
frame = wx.Frame(None,title = "Nhóm Tivi",size = (500,430))
panel = panel_Bai_7_2(frame)
panel.lstbox_dsnhom.Append(ds_ten_nhom_tivi)
frame.Show(True)
app.MainLoop()