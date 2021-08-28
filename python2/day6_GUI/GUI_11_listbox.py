import wx

def on_listbox(self):
	dlg = wx.MessageDialog(None, lst.GetStringSelection(), 'Thông báo', wx.OK)
	dlg.ShowModal()

app = wx.App()
frame = wx.Frame(None, title="Listbox", size=(300, 150))
panel = wx.Panel(frame, -1)

languages = ['C', 'C++', 'Java', 'Python', 'Perl']
lst = wx.ListBox(panel, size=(100, -1), pos=(10, 10), choices=languages, style=wx.LB_SINGLE)
frame.Bind(wx.EVT_LISTBOX, on_listbox, lst)

frame.Show(True)
app.MainLoop()
