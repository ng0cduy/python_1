import wx


def on_exit(event):
	frame.Close()


app = wx.App()
frame = wx.Frame(None, title="Menu", size=(500, 350))
panel = wx.Panel(frame, -1)

menu_bar = wx.MenuBar()

# Menu File: Menu cha
menu_file = wx.Menu()
menu_bar.Append(menu_file, "&File")

# Menu Thêm mới: Menu con của File
hinh_them_moi = wx.Bitmap('image/im1.png', wx.BITMAP_TYPE_ANY)
menu_them_moi = wx.MenuItem(menu_file, -1, text="Thêm mới")
menu_them_moi.SetBitmap(hinh_them_moi)
menu_file.Append(menu_them_moi)

# Menu Đóng: Menu con của File
menu_dong = wx.MenuItem(menu_file, -1, text="Đóng")
menu_file.Append(menu_dong)

# Menu Edit: Menu cha
menu_edit = wx.Menu()
menu_bar.Append(menu_edit, "&Edit")

# Menu Help: Menu cha
menu_help = wx.Menu()
menu_bar.Append(menu_help, "&Help")

frame.SetMenuBar(menu_bar)
frame.Bind(wx.EVT_MENU, on_exit, menu_dong)

frame.Show(True)
app.MainLoop()




