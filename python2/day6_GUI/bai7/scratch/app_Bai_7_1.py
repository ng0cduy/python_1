from giao_dien.gd_Bai_7_1 import *
from thu_vien.c_Cong_ty import *
from thu_vien.XL_Chung import *


# Khởi tạo đối tượng CongTy
xl_cong_ty = CongTy(duong_dan_cong_ty)
ds_cong_ty = xl_cong_ty.doc_thong_tin_cong_ty()[0]
print(ds_cong_ty)


app = wx.App()
frame = wx.Frame(None, title="Thông tin công ty", size=(520, 460))

panel = panel_Bai_7_1(frame)
panel.txtTen.SetValue(ds_cong_ty['Ten'])
panel.txtMaSo.SetValue(ds_cong_ty['Ma_so'])
panel.txtDienThoai.SetValue(ds_cong_ty['Dien_thoai'])
panel.txtDiaChi.SetValue(ds_cong_ty['Dia_chi'])
panel.txtEmail.SetValue(ds_cong_ty['Email'])

frame.Show(True)
app.MainLoop()

xl_cong_ty.disconnect()
