#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: To demo add menu, toolbar and statusbar to a frame.
#-----------------------------------------------------------------------------

import wx
import images

class Frame(wx.Frame):

    def __init__(self, parent=None, id=-1):
        super(self.__class__, self).__init__(parent=parent, id=id, title='Toolbars', size=(700, 400))

        #### create panel
        panel = wx.Panel(parent=self)
        panel.SetBackgroundColour(colour='White')

        #### create tool bar
        toolBar = self.CreateToolBar()
        # add tool to the tool bar
        # toolBar.AddTool(id=wx.NewId(), bitmap=images.getNewBitmap(), shortHelpString='New', longHelpString='Long help for New')
        toolBar.AddSimpleTool(id=wx.NewId(), bitmap=images.getNewBitmap(), shortHelpString='New', longHelpString='Long help for New')
        # preparing the tool bar to display
        self.SetToolBar(toolbar=toolBar)
        toolBar.Realize()

        #### create status bar
        statusBar = self.CreateStatusBar()
        self.SetStatusBar(statBar=statusBar)

        # create two individual menus
        m1 = wx.Menu()
        m2 = wx.Menu()

        m1.Append(id=wx.NewId(), text='&New', help='Create a new empty file')
        m1.AppendSeparator()
        exit_m = m1.Append(id=wx.NewId(), text='E&xit', help='Exit the program')

        m2.Append(id=wx.NewId(), text='&Copy', help='Copy in status bar')
        m2.Append(id=wx.NewId(), text='C&ut', help='None info')
        m2.Append(id=wx.NewId(), text='&Paste', help='None info also')
        m2.AppendSeparator()
        m2.Append(id=wx.NewId(), text='&Options...', help='Display options')

        #### create menu bar
        mb = wx.MenuBar()
        # attach the two indvidual menus to menu bar
        mb.Append(menu=m1, title='&File')
        mb.Append(menu=m2, title='&Edit')
        # attach the menu bar to the frame
        self.SetMenuBar(menubar=mb)

        #### create a menu event bound
        self.Bind(event=wx.EVT_MENU, handler=self.OnClose, source=exit_m)

        self.CenterOnScreen()

    def OnClose(self, event):
        self.Close()

class App(wx.App):

    def OnInit(self):
        self.frame = Frame()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()




