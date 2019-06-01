#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Use MDI (Multiple Document Interface).
#-----------------------------------------------------------------------------

import wx

class Frame(wx.MDIParentFrame):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='MDI Parent Frame', size=(600, 400))

        # m = wx.Menu()
        # new = m.Append(id=-1, text='&New Window')
        # m.AppendSeparator()
        # exit = m.Append(id=-1, text='E&xit')

        # self.Bind(event=wx.EVT_MENU, handler=self.OnNewWindow, source=new)
        # self.Bind(event=wx.EVT_MENU, handler=self.OnExit, source=exit)

        NEW_WINDOW_ID = 6000
        EXIT_ID       = 6001

        m = wx.Menu()
        m.Append(id=NEW_WINDOW_ID, text='&New Window')
        m.AppendSeparator()
        m.Append(id=EXIT_ID, text='E&xit')

        self.Bind(event=wx.EVT_MENU, handler=self.OnNewWindow, id=NEW_WINDOW_ID)
        self.Bind(event=wx.EVT_MENU, handler=self.OnExit, id=EXIT_ID)

        mb = wx.MenuBar()
        mb.Append(menu=m, title='&File')
        self.SetMenuBar(mb)

        self.CenterOnScreen()

    def OnNewWindow(self, event):
        frm = wx.MDIChildFrame(parent=self, id=-1, title='MDI Child Window')
        frm.Show()

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



