import wx
def on_click(self):
    item = self.GetItem()
    print(item.GetText())


players = [('TV001', 'Tivi Sony 49 inch', '12000000'), ('TV0010', 'Tivi Sony 50 inch', '15000000'),
       	('TV003', 'Tivi Sony 32 inch', '7000000'), ('TV004', 'Tivi LG 50 inch', '13000000'),
       	('TV005', 'Tivi Samsung 50 inch', '13500000')]

app = wx.App()
frame = wx.Frame(None, title="ListCtrl", size=(450, 200))
panel = wx.Panel(frame, -1)

lst = wx.ListCtrl(panel, -1, style=wx.LC_REPORT, size=(450, 200))
lst.InsertColumn(0, 'Mã số', width=100)
lst.InsertColumn(1, 'Tên', wx.LIST_FORMAT_LEFT, 200)
lst.InsertColumn(2, 'Giá', wx.LIST_FORMAT_RIGHT, 100)

for i in players:
	index = lst.GetItemCount()
	print(index)

	# lst.InsertStringItem(index, i[0])
	# lst.SetStringItem(index, 1, i[1])
	# lst.SetStringItem(index, 2, i[2])
	lst.InsertItem(index, i[0])
	lst.SetItem(index, 1, i[1])
	lst.SetItem(index, 2, i[2])
    

lst.Bind(wx.EVT_LIST_ITEM_SELECTED, on_click)

frame.Show(True)
app.MainLoop()




