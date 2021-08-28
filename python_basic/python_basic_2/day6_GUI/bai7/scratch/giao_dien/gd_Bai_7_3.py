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
from thu_vien.c_Nhan_vien import *

###########################################################################
## Class panel_Bai_7_3
###########################################################################

class panel_Bai_7_3 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 400,270 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"THÔNG TIN NHÂN VIÊN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		self.m_staticText8.SetFont( wx.Font( 20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )
		self.m_staticText8.SetForegroundColour( wx.Colour( 0, 0, 255 ) )

		bSizer3.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		gbSizer3 = wx.GridBagSizer( 0, 0 )
		gbSizer3.SetFlexibleDirection( wx.BOTH )
		gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Họ tên", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		self.m_staticText9.SetForegroundColour( wx.Colour( 0, 0, 0 ) )

		gbSizer3.Add( self.m_staticText9, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txtHoTen = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		gbSizer3.Add( self.txtHoTen, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Mã số", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		gbSizer3.Add( self.m_staticText10, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txtMaSo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		gbSizer3.Add( self.txtMaSo, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Tên đăng nhập", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		gbSizer3.Add( self.m_staticText11, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txtTenDangNhap = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		gbSizer3.Add( self.txtTenDangNhap, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Mật khẩu", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		gbSizer3.Add( self.m_staticText12, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txtMatKhau = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), wx.TE_PASSWORD )
		gbSizer3.Add( self.txtMatKhau, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Xác nhận Mật khẩu", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		gbSizer3.Add( self.m_staticText13, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txtXNMatKhau = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), wx.TE_PASSWORD )
		gbSizer3.Add( self.txtXNMatKhau, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.btnThem = wx.Button( self, wx.ID_ANY, u"Thêm", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer3.Add( self.btnThem, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer3.Add( gbSizer3, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		# Connect Events
		self.btnThem.Bind( wx.EVT_BUTTON, self.btnThem_click )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btnThem_click( self, event ):
		# Khởi tạo NhanVien
		xl_nhan_vien = NhanVien(duong_dan_nhan_vien)

		# Gán biến
		ma_so = self.txtMaSo.GetValue()
		ho_ten = self.txtHoTen.GetValue()
		ten_dang_nhap = self.txtTenDangNhap.GetValue()
		mat_khau = self.txtMatKhau.GetValue()
		xn_mat_khau = self.txtXNMatKhau.GetValue()

		# Thực hiện thêm
		if mat_khau == xn_mat_khau:
			kq = xl_nhan_vien.them_nhan_vien(ma_so, ho_ten, ten_dang_nhap, mat_khau)
			if kq != 0:
				self.txtMaSo.SetValue("")
				self.txtHoTen.SetValue("")
				self.txtTenDangNhap.SetValue("")
				self.txtMatKhau.SetValue("")
				self.txtXNMatKhau.SetValue("")
				wx.MessageBox("Thêm dữ liệu thành công.", "Thông báo", wx.OK | wx.ICON_INFORMATION)
			else:
				wx.MessageBox("Thêm dữ liệu thất bại.", "Thông báo", wx.OK | wx.ICON_ERROR)
		else:
			wx.MessageBox("Mật khẩu và Xác nhận Mật khẩu không khớp.", "Thông báo", wx.OK | wx.ICON_ERROR)
