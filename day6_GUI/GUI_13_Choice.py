import wx

def on_click(self):
	item = self.GetString()
	print(item)

app = wx.App()
frame = wx.Frame(None, title="Choice", size=(300, 150))
panel = wx.Panel(frame, -1)

sampleList = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight']
wx.StaticText(panel, -1, "Select one:", (15, 20))
choice = wx.Choice(panel, -1, (85, 18), choices=sampleList)

choice.Bind(wx.EVT_CHOICE, on_click)

frame.Show(True)
app.MainLoop()



