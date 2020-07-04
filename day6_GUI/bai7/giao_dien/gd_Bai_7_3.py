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
from thu_vien.c_NhanVien import *
    ###########################################################################
    ## Class panel_Bai_7_3
    ###########################################################################
class panel_Bai_7_3 ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,350 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        Them_nhan_vien = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"THÔNG TIN NHÂN VIÊN", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )

        self.m_staticText9.SetFont( wx.Font( 20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Berlin Sans FB" ) )
        self.m_staticText9.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

        Them_nhan_vien.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        gbSizer3 = wx.GridBagSizer( 0, 0 )
        gbSizer3.SetFlexibleDirection( wx.BOTH )
        gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.ho_ten = wx.StaticText( self, wx.ID_ANY, u"Họ tên", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.ho_ten.Wrap( -1 )

        gbSizer3.Add( self.ho_ten, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.txt_ho_ten = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 320,-1 ), 0 )
        gbSizer3.Add( self.txt_ho_ten, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.ma_so = wx.StaticText( self, wx.ID_ANY, u"Mã số", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.ma_so.Wrap( -1 )

        gbSizer3.Add( self.ma_so, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.txt_maso = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 320,-1 ), 0 )
        gbSizer3.Add( self.txt_maso, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.ten_dang_nhap = wx.StaticText( self, wx.ID_ANY, u"Tên đăng nhập", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.ten_dang_nhap.Wrap( -1 )

        gbSizer3.Add( self.ten_dang_nhap, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.txt_ten_dang_nhap = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 320,-1 ), 0 )
        gbSizer3.Add( self.txt_ten_dang_nhap, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.mat_khau = wx.StaticText( self, wx.ID_ANY, u"Mật khẩu", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.mat_khau.Wrap( -1 )

        gbSizer3.Add( self.mat_khau, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.txt_mat_khau = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 320,-1 ), 0 )
        gbSizer3.Add( self.txt_mat_khau, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.xac_nhan_mat_khau = wx.StaticText( self, wx.ID_ANY, u"Xác nhận mật khẩu", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.xac_nhan_mat_khau.Wrap( -1 )

        gbSizer3.Add( self.xac_nhan_mat_khau, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.btn_them = wx.Button( self, wx.ID_ANY, u"Thêm", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer3.Add( self.btn_them, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.txt_xac_nhan_mat_khau = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 320,-1 ), 0 )
        gbSizer3.Add( self.txt_xac_nhan_mat_khau, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


        Them_nhan_vien.Add( gbSizer3, 1, wx.EXPAND, 5 )


        self.SetSizer( Them_nhan_vien )
        self.Layout()

        # Connect Events
        self.btn_them.Bind( wx.EVT_BUTTON, self.btn_them_click )

    def __del__( self ):
        pass
	# Virtual event handlers, overide them in your derived class
    def btn_them_click( self, event ):
        xl_nhan_vien = NhanVien(duong_dan_nhan_vien)
        ma_so = self.txt_maso.GetValue()
        ho_ten = self.txt_ho_ten.GetValue()
        ten_dang_nhap =  self.txt_ten_dang_nhap.GetValue()
        mat_khau = self.txt_mat_khau.GetValue()
        xn_mat_khau = self.txt_xac_nhan_mat_khau.GetValue()

        #thuc hien them
        if mat_khau == xn_mat_khau:
            kq = xl_nhan_vien.them_nhan_vien(ma_so,ho_ten,ten_dang_nhap,mat_khau)
            if kq !=0:
                wx.MessageBox("Success","Thong bao",wx.OK|wx.ICON_INFORMATION)
            else:
                wx.MessageBox("Fail",wx.OK|wx.ICON_ERROR)
        else:
                wx.MessageBox("Fail",wx.OK|wx.ICON_ERROR)

