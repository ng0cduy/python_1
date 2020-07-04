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

###########################################################################
## Class panel_Bai_7_2
###########################################################################

class panel_Bai_7_2 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Nhóm Tivi" ), wx.VERTICAL )

		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText6 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Mã số", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		gbSizer2.Add( self.m_staticText6, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txtMaSo = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.txtMaSo, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText7 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Tên", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		gbSizer2.Add( self.m_staticText7, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txtTen = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 270,-1 ), 0 )
		gbSizer2.Add( self.txtTen, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.btnThem = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Thêm", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.btnThem, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 4 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		sbSizer1.Add( gbSizer2, 1, wx.EXPAND, 5 )


		bSizer2.Add( sbSizer1, 0, wx.EXPAND, 5 )

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Danh sách nhóm" ), wx.VERTICAL )

		lstboxDSNhomChoices = []
		self.lstboxDSNhom = wx.ListBox( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, lstboxDSNhomChoices, 0 )
		sbSizer2.Add( self.lstboxDSNhom, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer2.Add( sbSizer2, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		# Connect Events
		self.btnThem.Bind( wx.EVT_BUTTON, self.btnThem_click )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btnThem_click( self, event ):
		# Khởi tạo đối tượng NhomTivi
		xl_nhom_tivi = NhomTivi(duong_dan_tivi)

		# Gán biến
		ma_so = self.txtMaSo.GetValue()
		ten = self.txtTen.GetValue()

		# Thực hiện chức năng Thêm
		kq = xl_nhom_tivi.them_nhom_tivi(ma_so, ten)

		# Xuất kết quả
		if kq != 0:
			self.lstboxDSNhom.Append(ten)
			self.txtMaSo.SetValue("")
			self.txtTen.SetValue("")
			wx.MessageBox('Thêm thông tin thành công', 'Thông báo', wx.OK | wx.ICON_INFORMATION)
		else:
			wx.MessageBox('Thêm thông tin thất bại', 'Thông báo', wx.OK | wx.ICON_ERROR)

