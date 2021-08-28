from giao_dien.gd_Bai_7_3 import *

app=wx.App()
frame = wx.Frame(None,title="Thêm nhân viên",size=(520,370))
panel = panel_Bai_7_3(frame)
frame.Show(True)
app.MainLoop()