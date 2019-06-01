#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Set grid row & column header. (default is 1, 2, 3, ... and A, B, C, ...)
#-----------------------------------------------------------------------------

import wx
import wx.grid

class Frame(wx.Frame):

    rowLabels = ['one', 'two', 'three', 'four', 'five']
    colLabels = ['1st', '2nd', '3rd', '4th', '5th']

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, title='Grid Headers', size=(700, 500))

        g = wx.grid.Grid(parent=self)
        g.CreateGrid(numRows=5, numCols=5)

        for row in range(5):
            g.SetRowLabelValue(row, self.rowLabels[row])
            g.SetColLabelValue(row, self.colLabels[row])
            for col in range(5):
                g.SetCellValue(row=row, col=col, s='(%s, %s)' % (self.rowLabels[row], self.colLabels[col]))

class App(wx.App):

    def OnInit(self):
        frame = Frame()
        frame.Show()
        self.SetTopWindow(frame)
        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()




