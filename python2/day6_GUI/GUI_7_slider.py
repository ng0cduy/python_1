import wx


def on_xem_1(self):
	dlg = wx.MessageDialog(None, "Slide 1 : value = " + str(slider1.GetRange()), 'A Message Box', wx.OK)
	dlg.ShowModal()


def on_xem_2(self):
	dlg = wx.MessageDialog(None, "Slide 2 : value = " + str(slider2.GetRange()), 'A Message Box', wx.OK)
	dlg.ShowModal()


app = wx.App()
frame = wx.Frame(None, title="Slider", size=(400, 500))
panel = wx.Panel(frame, -1)

slider1 = wx.Slider(panel, -1, 30, 1, 100, pos=(10, 10), size=(250, -1),
                	style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS | wx.SL_LABELS)

slider2 = wx.Slider(panel, -1, 25, 1, 100, pos=(125, 50), size=(-1, 250),
                	style=wx.SL_VERTICAL | wx.SL_AUTOTICKS | wx.SL_LABELS | wx.SL_INVERSE)  # wx.SL_INVERSE dùng để đảo Slider

btnXem1 = wx.Button(panel, label="Xem", pos=(300, 10), size=(50, 30))
frame.Bind(wx.EVT_BUTTON, on_xem_1, btnXem1)

btnXem2 = wx.Button(panel, label="Xem", pos=(200, 250), size=(50, 30))
frame.Bind(wx.EVT_BUTTON, on_xem_2, btnXem2)


frame.Show(True)
app.MainLoop()



