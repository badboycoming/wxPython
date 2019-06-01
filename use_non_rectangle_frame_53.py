#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Use non rectangle frame.
#-----------------------------------------------------------------------------

import wx
import images

class Frame(wx.Frame):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='Shaped Frame',
                                             style=wx.FRAME_SHAPED | wx.SIMPLE_BORDER | wx.FRAME_NO_TASKBAR)
        self.hasShape = False

        # get image
        self.bmp = images.getVippiBitmap()
        self.SetClientSize(size=(self.bmp.GetWidth(), self.bmp.GetHeight()))

        # draw
        dc = wx.ClientDC(win=self)
        dc.DrawBitmap(bmp=self.bmp, x=0, y=0, useMask=True)

        self.setWindowShape()
        self.Bind(event=wx.EVT_LEFT_DCLICK, handler=self.OnDoubleClick)
        self.Bind(event=wx.EVT_RIGHT_UP, handler=self.OnExit)
        self.Bind(event=wx.EVT_PAINT, handler=self.OnPaint)
        self.Bind(event=wx.EVT_WINDOW_CREATE, handler=self.setWindowShape)  # Note force binding

        self.CenterOnScreen()

    def setWindowShape(self, event=None):  # due to for GTK, have event, for MS-Windows, no event, so set event default to None
        r = wx.RegionFromBitmap(bmp=self.bmp)
        self.hasShape = self.SetShape(region=r)

    def OnDoubleClick(self, event):
        if self.hasShape:
            self.SetShape(wx.Region())  # use empty region for SetShape, get a rectangle
            self.hasShape = False
        else:
            self.setWindowShape()

    def OnExit(self, event):
        self.Close()

    def OnPaint(self, event):
        dc = wx.PaintDC(win=self)
        dc.DrawBitmap(bmp=self.bmp, x=0, y=0, useMask=True)

class App(wx.App):

    def OnInit(self):
        frame = Frame()
        frame.Show()
        self.SetTopWindow(frame)
        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()





