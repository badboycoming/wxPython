#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Use scroll window.
#-----------------------------------------------------------------------------

import wx

class Frame(wx.Frame):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='Scroll Frame', size=(500, 300))

        self.scroll = wx.ScrolledWindow(parent=self, id=-1)
        self.scroll.SetScrollbars(pixelsPerUnitX=1, pixelsPerUnitY=1, noUnitsX=700, noUnitsY=500)

        btn = wx.Button(parent=self.scroll, id=-1, label='Scroll Me', pos=(50, 20))
        btn2 = wx.Button(parent=self.scroll, id=-1, label='Scroll Back', pos=(550, 450))
        self.Bind(event=wx.EVT_BUTTON, handler=self.OnClickTop, source=btn)
        self.Bind(event=wx.EVT_BUTTON, handler=self.OnClickBottom, source=btn2)

        self.CenterOnScreen()

    def OnClickTop(self, event):
        self.scroll.Scroll(700, 500)

    def OnClickBottom(self, event):
        self.scroll.Scroll(1, 1)

class App(wx.App):

    def OnInit(self):
        frame = Frame()
        frame.Show()
        self.SetTopWindow(frame)
        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()



