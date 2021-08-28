import wx
def on_clicked(self):
    cb = self.GetEventObject()
    print(cb.GetLabel(), 'is clicked', cb.GetValue())


app = wx.App()
frame = wx.Frame(None, title="Checkbox", size=(300, 150))
panel = wx.Panel(frame, -1)

wx.CheckBox(panel, -1, "Một", (35, 40), (150, 20))
wx.CheckBox(panel, -1, "Hai", (35, 60), (150, 20))
wx.CheckBox(panel, -1, "Ba", (35, 80), (150, 20))

frame.Bind(wx.EVT_CHECKBOX, on_clicked)

frame.Show(True)
app.MainLoop()
