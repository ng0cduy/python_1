import wx
app = wx.App()
window = wx.Frame (None,title ="wxPython Frame",size = (500,500))
panel  = wx.Panel(window)
label  = wx.StaticText(panel,label="Hello World",pos=(200,200))
window.Show(True)
app.MainLoop()