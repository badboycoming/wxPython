#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Basic grid sizer.
#-----------------------------------------------------------------------------

import wx
from blockwindow import BlockWindow

labels = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

class GridSizerFrame(wx.Frame):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='Basic Grid Sizer')
        sizer = wx.GridSizer(rows=3, cols=3, hgap=5, vgap=5)

        for label in labels:
            bw = BlockWindow(parent=self, label=label)
            sizer.Add(item=bw, proportion=0, flag=0, border=0)

        self.SetSizer(sizer)
        self.Fit()

class GridSizerApp(wx.App):

    def OnInit(self):
        frame = GridSizerFrame()
        frame.Show()
        self.SetTopWindow(frame)
        return True

if __name__ == '__main__':

    app = GridSizerApp()
    app.MainLoop()



