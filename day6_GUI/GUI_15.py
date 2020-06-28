import wx


app = wx.App()
frame = wx.Frame(None, title="Image", size=(633, 442))
panel = wx.Panel(frame, -1)

hinh = wx.Image("images/honda-cr-v-2020-28349.png", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
stStaticBitmap = wx.StaticBitmap(panel, -1, hinh, style=wx.CENTER)

frame.Show(True)
app.MainLoop()



