#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: A pre-defined block window, for other module import to test every sizer scheme.
#-----------------------------------------------------------------------------

import wx

class BlockWindow(wx.Panel):

    def __init__(self, parent, id=-1, label='', pos=wx.DefaultPosition, size=(100, 25)):
        super(self.__class__, self).__init__(parent=parent, id=id, pos=pos, size=size,
                                             style=wx.RAISED_BORDER, name=label)
        self.label = label
        self.SetBackgroundColour('white')
        self.SetMinSize(size)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, event):
        sz = self.GetClientSize()
        dc = wx.PaintDC(self)
        w, h = dc.GetTextExtent(self.label)
        dc.SetFont(self.GetFont())
        dc.DrawText(self.label, (sz.width-w)/2, (sz.height-h)/2)  # make the label in the center of the panel

#-----------------------------------------------------------------------------

class Frame(wx.Frame):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='test')
        panel1 = BlockWindow(parent=self, label='first')
        panel2 = BlockWindow(parent=self, pos=(100, 25), label='second')

class App(wx.App):

    def OnInit(self):
        frame = Frame()
        frame.Show()
        self.SetTopWindow(frame)
        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()




