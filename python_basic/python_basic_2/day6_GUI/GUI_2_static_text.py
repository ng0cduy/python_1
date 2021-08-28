import wx
app = wx.App()
frame = wx.Frame (None,title ="Ví dụ StaticText",size = (500,500))
panel  = wx.Panel(frame,-1)
label  = wx.StaticText(panel,label="Hello World",style=wx.ALIGN_CENTER,size=(480,400),pos=(0,200))
frame.Show(True)
app.MainLoop()