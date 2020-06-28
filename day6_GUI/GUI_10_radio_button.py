import wx

def on_clicked(self):
	cb = self.GetEventObject()
	print(cb.GetLabel(), 'is clicked')


app = wx.App()
frame = wx.Frame(None, title="Checkbox", size=(300, 250))
panel = wx.Panel(frame, -1)

wx.RadioButton(panel, -1, "Nam", pos=(20, 10), style=wx.RB_GROUP)
wx.RadioButton(panel, -1, "Nữ", pos=(20, 40))
wx.RadioButton(panel, -1, "Khác", pos=(20, 70))

frame.Bind(wx.EVT_RADIOBUTTON, on_clicked)

frame.Show(True)
app.MainLoop()
