from giao_dien.gd_Bai_7_1 import *
from thu_vien.c_Cong_ty import *
from thu_vien.xu_ly_chung import*


xl_cong_ty = CongTy(duong_dan_cong_ty)
ds_cong_ty = xl_cong_ty.doc_thong_tin_cong_ty()[0]

# khởi tạo đối tượng công ty
app = wx.App()
frame = wx.Frame(None,title = "Thông tin công ty",size = (540,360))
panel = panel_Bai_7_1(frame)
panel.txt_ten.SetValue(ds_cong_ty['Ten'])
panel.txt_ma_so.SetValue(ds_cong_ty['Ma_so'])
panel.txt_dien_thoai.SetValue(ds_cong_ty['Dien_thoai'])
panel.txt_dia_chi.SetValue(ds_cong_ty['Dia_chi'])
panel.txt_email.SetValue(ds_cong_ty['Email'])

frame.Show(True)
app.MainLoop()