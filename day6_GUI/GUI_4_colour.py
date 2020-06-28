import wx
app = wx.App()
frame = wx.Frame (None,title ="Ví dụ StaticText",size = (500,500))
panel  = wx.Panel(frame,-1)
# str_  = "Thông tin công ty"
# text =wx.StaticText(panel,-1,str_,(20,20))
# font =wx.Font(18,wx.DECORATIVE,wx.ITALIC,wx.NORMAL)
# text.SetFont(font)

# text.setForegroundColour("0000FF")
# panel.SetBackgroundColour("CC99FF")

# wx.StaticText(panel,-1,"công ty trách nhiệm hữa hạn",(20,50))

label = wx.StaticText(panel, label="Hello cả lớp", style=wx.ALIGN_CENTER, size=(480, 400), pos=(0, 50))
font = wx.Font(18, wx.DECORATIVE, wx.BOLD, wx.NORMAL)
label.SetFont(font)

label.SetForegroundColour('#0000FF')
panel.SetBackgroundColour('#CC99FF')


txt1 = wx.TextCtrl(panel, value="Nhập họ tên", pos=(100, 250), size=(150, 30))
txt1.SetBackgroundColour('red')
frame.Show(True)
app.MainLoop()