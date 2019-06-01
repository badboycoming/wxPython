#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: To demo how to use module from package wx.py.
#-----------------------------------------------------------------------------

import wx
import images
from wx.py.shell import ShellFrame
from wx.py.filling import FillingFrame

class Frame(wx.Frame):

    def __init__(self, parent=None, id=-1):
        super(self.__class__, self).__init__(parent=parent, id=id, title='Use Py Packages', size=(500, 300))

        self.panel = wx.Panel(parent=self)
        self.panel.SetBackgroundColour('White')

        self.sb = self.CreateStatusBar()
        self.SetStatusBar(statBar=self.sb)

        self.tb = self.CreateToolBar()
        self.tb.AddTool(id=wx.NewId(), bitmap=images.getNewBitmap(), shortHelpString='New', longHelpString='Long help for New')
        self.tb.Realize()
        self.SetToolBar(self.tb)

        m1 = wx.Menu()
        m1.Append(id=wx.NewId(), text='&Open', help='Open a file')
        m1.AppendSeparator()
        exit = m1.Append(id=wx.NewId(), text='E&xit', help='Exit and close')

        m2 = wx.Menu()
        m2.Append(id=wx.NewId(), text='&Copy', help='')
        m2.Append(id=wx.NewId(), text='C&ut', help='')
        m2.Append(id=wx.NewId(), text='&Paste', help='')
        m2.AppendSeparator()
        m2.Append(id=wx.NewId(), text='&Options...', help='')

        m3 = wx.Menu()
        shell = m3.Append(id=wx.NewId(), text='&Python shell', help='Open Python shell frame')
        filling = m3.Append(id=wx.NewId(), text='&Namespace viewer', help='Open namespace viewer frame')

        mb = wx.MenuBar()
        mb.Append(menu=m1, title='&File')
        mb.Append(menu=m2, title='&Edit')
        mb.Append(menu=m3, title='&Debug')
        self.SetMenuBar(mb)

        self.Bind(event=wx.EVT_MENU, handler=self.OnClose, source=exit)
        self.Bind(event=wx.EVT_MENU, handler=self.OnShell, source=shell)
        self.Bind(event=wx.EVT_MENU, handler=self.OnFilling, source=filling)

        self.CenterOnScreen()

    def OnClose(self, event):
        self.Close()

    def OnShell(self, event):
        subframe = ShellFrame(parent=self)
        subframe.Show()
        # subframe.CenterOnScreen()

    def OnFilling(self, event):
        subframe = FillingFrame(parent=self)
        subframe.Show()
        # subframe.CenterOnScreen()

class App(wx.App):

    def OnInit(self):
        self.frame = Frame()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()





