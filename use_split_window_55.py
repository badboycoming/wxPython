#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Use split window.
#-----------------------------------------------------------------------------

import wx

class Frame(wx.Frame):

    def __init__(self, parent=None, title='Split Window'):
        super(self.__class__, self).__init__(parent=parent, title=title, size=(900, 700))
        self.__MakeMenuBar()

        self.initPos = 300
        self.sp = wx.SplitterWindow(parent=self, style=wx.SP_LIVE_UPDATE)
        self.p1 = wx.Panel(parent=self.sp, style=wx.SUNKEN_BORDER)
        self.p2 = wx.Panel(parent=self.sp, style=wx.SUNKEN_BORDER)
        self.p2.Hide()
        self.p1.SetBackgroundColour('pink')
        self.p2.SetBackgroundColour('sky blue')
        self.sp.Initialize(self.p1)
        self.sp.SetMinimumPaneSize(10)

        self.CenterOnScreen()

    def __MakeMenuBar(self):

        menu = wx.Menu()

        item = menu.Append(id=-1, text='Split horizontally')
        self.Bind(event=wx.EVT_MENU, handler=self.OnSplitH, source=item)
        self.Bind(event=wx.EVT_UPDATE_UI, handler=self.OnCheckCanSplit, source=item)  # NOTE, control the menu item active or not

        item = menu.Append(id=-1, text='Split vertically')
        self.Bind(event=wx.EVT_MENU, handler=self.OnSplitV, source=item)
        self.Bind(event=wx.EVT_UPDATE_UI, handler=self.OnCheckCanSplit, source=item)  # NOTE, control the menu item active or not

        item = menu.Append(id=-1, text='Unsplit')
        self.Bind(event=wx.EVT_MENU, handler=self.OnUnSplit, source=item)
        self.Bind(event=wx.EVT_UPDATE_UI, handler=self.OnCheckCanUnsplit, source=item)  # NOTE, control the menu item active or not

        menu.AppendSeparator()

        item = menu.Append(id=wx.ID_EXIT, text='E&xit')
        self.Bind(event=wx.EVT_MENU, handler=self.OnExit, source=item)

        mbar = wx.MenuBar()
        mbar.Append(menu=menu, title='&Splitter')
        self.SetMenuBar(mbar)

    def OnSplitH(self, event):
        self.sp.SplitHorizontally(self.p1, self.p2, self.initPos)

    def OnSplitV(self, event):
        self.sp.SplitVertically(self.p1, self.p2, self.initPos)

    def OnCheckCanSplit(self, event):
        event.Enable(not self.sp.IsSplit())

    def OnCheckCanUnsplit(self, event):
        event.Enable(self.sp.IsSplit())

    def OnUnSplit(self, event):
        self.sp.Unsplit()

    def OnExit(self, event):
        self.Close()

class App(wx.App):

    def OnInit(self):
        frame = Frame()
        frame.Show()
        self.SetTopWindow(frame)
        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()



