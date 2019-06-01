#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Resize grid sizer.
#-----------------------------------------------------------------------------

import wx
from blockwindow import BlockWindow

labels = 'one two three four five six seven eight nine'.split()
flags = {'one': wx.ALIGN_BOTTOM, 'two': wx.ALIGN_CENTER,
         'four': wx.ALIGN_RIGHT, 'six': wx.EXPAND, 'seven': wx.EXPAND,
         'eight': wx.SHAPED}

class Frame(wx.Frame):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='Grid Sizer Resize')
        sizer = wx.GridSizer(rows=3, cols=3, hgap=5, vgap=5)
        for label in labels:
            bw = BlockWindow(parent=self, label=label)
            flag = flags.get(label, 0)
            sizer.Add(item=bw, proportion=0, flag=flag, border=0)
        self.SetSizer(sizer)
        self.Fit()

class App(wx.App):

    def OnInit(self):
        self.frame = Frame()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()





