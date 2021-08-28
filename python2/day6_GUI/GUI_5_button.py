import wx
def on_click(self):
    btn.SetLabel ("Đã click")
app = wx.App()
frame = wx.Frame (None,title ="Ví dụ Button",size = (500,500))
panel  = wx.Panel(frame)

btn = wx.Button(panel,label = 'Cick xem kq',pos=(100,100))
frame.Bind(wx.EVT_BUTTON,on_click,btn)

frame.Show(True)
app.MainLoop()