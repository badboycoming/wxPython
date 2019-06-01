#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Resize flex grid sizer.
#-----------------------------------------------------------------------------

import wx
from blockwindow import BlockWindow

labels = 'one two three four five six seven eight nine'.split()

class Frame(wx.Frame):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='Resize Flex Grid Sizer')
        sizer = wx.FlexGridSizer(rows=3, cols=3, hgap=5, vgap=5)
        for label in labels:
            bw = BlockWindow(parent=self, label=label)
            sizer.Add(item=bw, proportion=0, flag=0)
        center = self.FindWindowByName('five')
        center.SetMinSize((150, 50))

        sizer.AddGrowableCol(idx=0, proportion=1)
        sizer.AddGrowableCol(idx=1, proportion=2)
        sizer.AddGrowableCol(idx=2, proportion=1)

        sizer.AddGrowableRow(idx=0, proportion=1)
        sizer.AddGrowableRow(idx=1, proportion=5)
        sizer.AddGrowableRow(idx=2, proportion=1)

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



