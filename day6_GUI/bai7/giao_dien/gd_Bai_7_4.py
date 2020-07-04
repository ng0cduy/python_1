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
from thu_vien.c_TIVI import *

###########################################################################
## Class panel_Bai 7_4
###########################################################################

class panel_Bai_7_4 ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1000,320 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer4 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"THÔNG TIN TIVI", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText15.Wrap( -1 )

        bSizer4.Add( self.m_staticText15, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        gbSizer4 = wx.GridBagSizer( 0, 0 )
        gbSizer4.SetFlexibleDirection( wx.BOTH )
        gbSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Mã số", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText16.Wrap( -1 )

        gbSizer4.Add( self.m_staticText16, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.txt_ma_so = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
        gbSizer4.Add( self.txt_ma_so, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"Tên", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText17.Wrap( -1 )

        gbSizer4.Add( self.m_staticText17, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.txt_ten = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
        gbSizer4.Add( self.txt_ten, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"Ký hiệu", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText18.Wrap( -1 )

        gbSizer4.Add( self.m_staticText18, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.txt_ky_hieu = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
        gbSizer4.Add( self.txt_ky_hieu, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Đơn giá nhập", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText19.Wrap( -1 )

        gbSizer4.Add( self.m_staticText19, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.txt_don_gia_nhap = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
        gbSizer4.Add( self.txt_don_gia_nhap, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Đơn giá bán", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText21.Wrap( -1 )

        gbSizer4.Add( self.m_staticText21, wx.GBPosition( 3, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.txt_don_gia_ban = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 345,-1 ), 0 )
        gbSizer4.Add( self.txt_don_gia_ban, wx.GBPosition( 3, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"Số lượng tồn", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText20.Wrap( -1 )

        gbSizer4.Add( self.m_staticText20, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.txt_so_luong_ton = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
        gbSizer4.Add( self.txt_so_luong_ton, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"Nhóm Tivi", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText22.Wrap( -1 )

        gbSizer4.Add( self.m_staticText22, wx.GBPosition( 4, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        choice_nhom_tvChoices = []
        self.choice_nhom_tv = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 345,-1 ), choice_nhom_tvChoices, 0 )
        self.choice_nhom_tv.SetSelection( 0 )
        gbSizer4.Add( self.choice_nhom_tv, wx.GBPosition( 4, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.btn_them = wx.Button( self, wx.ID_ANY, u"Thêm", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer4.Add( self.btn_them, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 4 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer4.Add( gbSizer4, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer4 )
        self.Layout()

        # Connect Events
        self.choice_nhom_tv.Bind( wx.EVT_CHOICE, self.choice_nhom_tv_click )
        self.btn_them.Bind( wx.EVT_BUTTON, self.btn_them_click )

    def __del__( self ):
        pass


	# Virtual event handlers, overide them in your derived class
    def choice_nhom_tv_click( self, event ):
        xl_nhom_tv =NhomTivi(duong_dan_tivi)
        #gan bien
        ten_nhom = self.choice_nhom_tv.GetStringSelection()
        ma_so = xl_nhom_tv.lay_ma_so_tu_ten_nhom(ten_nhom)
        print(ma_so)
        return ma_so
        
    def btn_them_click( self, event ):
       #khoi tao TV
       xl_TV = Tivi(duong_dan_tivi)
       #gan bien
       ma_so = self.txt_ma_so.GetValue()
       ten = self.txt_ten.GetValue()
       ki_hieu = self.txt_ky_hieu.GetValue()
       don_gia_ban = self.txt_don_gia_ban.GetValue()
       don_gia_nhap = self.txt_don_gia_nhap.GetValue()
       so_luong_ton = self.txt_so_luong_ton.GetValue()
       Nhom_tivi = self.choice_nhom_tv_click()
       kq = xl_TV.them_tivi(ma_so,ten,ki_hieu,don_gia_ban,don_gia_nhap,so_luong_ton,Nhom_tivi)
       