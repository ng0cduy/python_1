# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from thu_vien.xu_ly_chung import *
from thu_vien.c_Nhom_Tivi import *

###########################################################################
## Class panel_Bai_7_2
###########################################################################

class panel_Bai_7_2 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.Point( -1,100 ), size = wx.Size( 500,411 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Nhóm Tivi" ), wx.VERTICAL )

		sbSizer1.SetMinSize( wx.Size( -1,200 ) )
		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText6 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Mã số", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		gbSizer2.Add( self.m_staticText6, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txt_ma_so = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.txt_ma_so, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText7 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Tên", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		gbSizer2.Add( self.m_staticText7, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txt_ten = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		gbSizer2.Add( self.txt_ten, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.btn_them = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Thêm", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.btn_them, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 4 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		sbSizer1.Add( gbSizer2, 1, wx.EXPAND, 5 )


		bSizer2.Add( sbSizer1, 1, wx.EXPAND, 5 )

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Danh sách nhóm" ), wx.VERTICAL )

		sbSizer2.SetMinSize( wx.Size( -1,200 ) )
		lstbox_dsnhomChoices = []
		self.lstbox_dsnhom = wx.ListBox( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, lstbox_dsnhomChoices, 0 )
		self.lstbox_dsnhom.SetMinSize( wx.Size( 480,150 ) )

		sbSizer2.Add( self.lstbox_dsnhom, 0, wx.ALL, 5 )


		bSizer2.Add( sbSizer2, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		# Connect Events
		self.btn_them.Bind( wx.EVT_BUTTON, self.btn_them_click )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_them_click( self, event ):
	    
        #khoi tao doi tuong nhom tv
		xl_nhom_TV = NhomTivi(duong_dan_tivi)

        #gán biến
		ma_so = self.txt_ma_so.GetValue()
		ten = self.txt_ten.GetValue()

        #Thuc hien chuc nang them
		kq = xl_nhom_TV.them_nhom_tivi(ma_so,ten)

        #xuat ket qua

		if (kq!=0):
			self.lstbox_dsnhom.Append(ten)
			self.txt_ma_so.SetValue("")
			self.txt_ten.SetValue("")
			wx.MessageBox('Them thong tin thanh cong','Thông báo', wx.OK|wx.ICON_INFORMATION)
		else:
			wx.MessageBox('Fail','Thông báo',wx.OK|wx.ICON_INFORMATION)

