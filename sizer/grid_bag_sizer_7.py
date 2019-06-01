#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: grid bag sizer.
#-----------------------------------------------------------------------------

import wx
from blockwindow import BlockWindow

labels = 'one two three four five six seven eight nine'.split()

class Frame(wx.Frame):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='Grid Bag Sizer')
        sizer = wx.GridBagSizer(hgap=5, vgap=5)

        for col in range(3):
            for row in range(3):
                bw = BlockWindow(parent=self, label=labels[row*3 + col])
                sizer.Add(item=bw, pos=(row, col))

        # add a window that spans several rows
        bw = BlockWindow(parent=self, label='span 3 row')
        sizer.Add(item=bw, pos=(0, 3), span=(3, 1), flag=wx.EXPAND)

        # add a window that spans all columns
        bw = BlockWindow(parent=self, label='span all columns')
        sizer.Add(item=bw, pos=(3, 0), span=(1, 4), flag=wx.EXPAND)

        # make the last row and last column be streatchable
        sizer.AddGrowableRow(3)
        sizer.AddGrowableCol(3)

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




