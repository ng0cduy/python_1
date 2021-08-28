# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

from thu_vien.XL_Chung import *
from thu_vien.c_Nhom_Tivi import *
from thu_vien.c_Tivi import *

###########################################################################
## Class panel_Bai_7_4
###########################################################################

class panel_Bai_7_4 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,260 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"THÔNG TIN TIVI", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		self.m_staticText14.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )
		self.m_staticText14.SetForegroundColour( wx.Colour( 255, 0, 0 ) )

		bSizer4.Add( self.m_staticText14, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		gbSizer4 = wx.GridBagSizer( 0, 0 )
		gbSizer4.SetFlexibleDirection( wx.BOTH )
		gbSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Mã số", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		gbSizer4.Add( self.m_staticText15, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txtMaSo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		gbSizer4.Add( self.txtMaSo, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Tên", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		gbSizer4.Add( self.m_staticText16, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txtTen = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		gbSizer4.Add( self.txtTen, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"Ký hiệu", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		gbSizer4.Add( self.m_staticText17, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txtKyHieu = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		gbSizer4.Add( self.txtKyHieu, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"Đơn giá nhập", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		gbSizer4.Add( self.m_staticText18, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txtDonGiaNhap = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		gbSizer4.Add( self.txtDonGiaNhap, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"Đơn giá bán", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		gbSizer4.Add( self.m_staticText20, wx.GBPosition( 3, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txtDonGiaBan = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		gbSizer4.Add( self.txtDonGiaBan, wx.GBPosition( 3, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Số lượng tồn", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		gbSizer4.Add( self.m_staticText19, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txtSoLuongTon = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		gbSizer4.Add( self.txtSoLuongTon, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Nhóm Tivi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		gbSizer4.Add( self.m_staticText21, wx.GBPosition( 4, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		choiceNhomTiviChoices = []
		self.choiceNhomTivi = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,-1 ), choiceNhomTiviChoices, 0 )
		self.choiceNhomTivi.SetSelection( 0 )
		gbSizer4.Add( self.choiceNhomTivi, wx.GBPosition( 4, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.btnThem = wx.Button( self, wx.ID_ANY, u"Thêm", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer4.Add( self.btnThem, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 4 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( gbSizer4, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		# Connect Events
		self.choiceNhomTivi.Bind( wx.EVT_CHOICE, self.choiceNhomTivi_click )
		self.btnThem.Bind( wx.EVT_BUTTON, self.btnThem_click )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def choiceNhomTivi_click( self, event ):
		# Khởi tạo NhomTivi
		xl_nhom_tivi = NhomTivi(duong_dan_tivi)

		# Gán biến
		ten_nhom = self.choiceNhomTivi.GetStringSelection()

		# Lấy mã số
		ma_so = xl_nhom_tivi.lay_ma_so_tu_ten_nhom(ten_nhom)
		print(ma_so)
		return ma_so

	def btnThem_click( self, event ):
		# Khởi tạo Tivi
		xl_tivi = Tivi(duong_dan_tivi)

		# Gán biến
		ma_so = self.txtMaSo.GetValue()
		ten = self.txtTen.GetValue()
		ky_hieu = self.txtKyHieu.GetValue()
		don_gia_ban = self.txtDonGiaBan.GetValue()
		don_gia_nhap = self.txtDonGiaNhap.GetValue()
		so_luong_ton = self.txtSoLuongTon.GetValue()
		nhom_tivi = self.choiceNhomTivi_click(self)

		kq = xl_tivi.them_tivi(ma_so, ten, ky_hieu, don_gia_ban, don_gia_nhap, so_luong_ton, nhom_tivi)
		if kq != 0:
			self.txtMaSo.SetValue("")
			self.txtTen.SetValue("")
			self.txtKyHieu.SetValue("")
			self.txtDonGiaBan.SetValue("")
			self.txtDonGiaNhap.SetValue("")
			self.txtSoLuongTon.SetValue("")
			wx.MessageBox("Thêm dữ liệu thành công.", "Thông báo", wx.OK | wx.ICON_INFORMATION)
		else:
			wx.MessageBox("Thêm dữ liệu thất bại.", "Thông báo", wx.OK | wx.ICON_ERROR)

