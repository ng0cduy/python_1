import wx
def on_click(self):
    btn.SetBitmap (image_2)
app = wx.App()
frame = wx.Frame (None,title ="Ví dụ Button",size = (500,500))
panel  = wx.Panel(frame,-1)
image_1  = wx.Image('image/im3.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap()
image_2  = wx.Image('image/im4.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap()

btn = wx.BitmapButton(panel,-1,image_1,pos=(100,100))

frame.Bind(wx.EVT_BUTTON,on_click,btn)

btn.SetDefault()

frame.Show(True)

app.MainLoop()


