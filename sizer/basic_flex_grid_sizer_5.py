#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Basic flex grid sizer.
#-----------------------------------------------------------------------------

import wx
from blockwindow import BlockWindow

labels = 'one two three four five six seven eight nine'.split()

class Frame(wx.Frame):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='Flex Grid Sizer')
        sizer = wx.FlexGridSizer(rows=3, cols=3, hgap=5, vgap=5)
        for label in labels:
            bw = BlockWindow(parent=self, label=label)
            sizer.Add(item=bw, proportion=0, flag=0)
        center = self.FindWindowByName('five')
        center.SetMinSize((150, 50))
        self.SetSizer(sizer)
        self.Fit()

        self.SetMinSize(self.GetSize())
        self.Center(wx.BOTH)

class App(wx.App):

    def OnInit(self):
        self.frame = Frame()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()



