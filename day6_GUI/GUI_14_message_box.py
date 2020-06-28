import wx


def on_xem(event):
	kq = wx.MessageBox("Bạn có chắc chắn muốn xóa không", "Thông báo", wx.YES | wx.NO)
	if wx.YES == kq:
		stTraLoi.SetLabel("Bạn chọn button YES")
	else:
		stTraLoi.SetLabel("Bạn chọn button NO")
	# if wx.OK == kq:
	# 	print("OK")
	# else:
	# 	print("NOT OK")


app = wx.App()
frame = wx.Frame(None, title="MessageBox", size=(300, 150))
panel = wx.Panel(frame, -1)

btnChon = wx.Button(panel, -1, label="Click vào để xem Message", pos=(10, 10))
frame.Bind(wx.EVT_BUTTON, on_xem, btnChon)
stTraLoi = wx.StaticText(panel, -1, pos=(10, 50))

frame.Show(True)
app.MainLoop()




