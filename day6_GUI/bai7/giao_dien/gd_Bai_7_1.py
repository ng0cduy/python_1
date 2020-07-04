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
from thu_vien.c_Cong_ty import *

###########################################################################
## Class panel_Bai_7_1
###########################################################################

class panel_Bai_7_1 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 520,400 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"image/katakana.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_bitmap1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Tên", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		gbSizer1.Add( self.m_staticText1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Mã số", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		gbSizer1.Add( self.m_staticText2, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txt_ma_so = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 380,-1 ), 0 )
		gbSizer1.Add( self.txt_ma_so, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Điện thoại", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		gbSizer1.Add( self.m_staticText3, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txt_dien_thoai = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 380,-1 ), 0 )
		gbSizer1.Add( self.txt_dien_thoai, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Địa chỉ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		gbSizer1.Add( self.m_staticText4, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txt_dia_chi = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 380,-1 ), 0 )
		gbSizer1.Add( self.txt_dia_chi, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txt_ten = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 380,-1 ), 0 )
		gbSizer1.Add( self.txt_ten, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Email", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		gbSizer1.Add( self.m_staticText5, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txt_email = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 380,-1 ), 0 )
		gbSizer1.Add( self.txt_email, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.btn_cap_nhat = wx.Button( self, wx.ID_ANY, u"Cập nhật", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.btn_cap_nhat, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer1.Add( gbSizer1, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		# Connect Events
		self.btn_cap_nhat.Bind( wx.EVT_BUTTON, self.btn_cap_nhat_click )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_cap_nhat_click( self, event ):
		#Khởi tạo object công ty
		xl_cong_ty = CongTy(duong_dan_cong_ty)
		#Khai báo biến:
		ten = self.txt_ten.GetValue()
		ma_so = self.txt_ma_so.GetValue()
		dien_thoai = self.txt_dien_thoai.GetValue()
		dia_chi = self.txt_dia_chi.GetValue()
		email = self.txt_email.GetValue()

		#thực hiện thao tác cập nhật
		kq = xl_cong_ty.cap_nhat_thong_tin_cong_ty(ten,ma_so,dien_thoai,dia_chi,email)
		if kq!=0:
			wx.MessageBox("Cập nhật thông tin thành công","Thông báo",wx.OK|wx.ICON_INFORMATION)
		else:
			wx.MessageBox("Fail","Thông báo",wx.OK|wx.ICON_ERROR)
		#Xuất thông báo

		xl_cong_ty.disconnect()