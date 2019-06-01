#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Basic grid. Use "CreateGrid" to create.
#-----------------------------------------------------------------------------

import wx
import wx.grid

class Frame(wx.Frame):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, title='Basic Grid', size=(700, 500))

        g = wx.grid.Grid(parent=self)
        g.CreateGrid(numRows=50, numCols=50)

        for row in range(20):
            for col in range(6):
                g.SetCellValue(row=row, col=col, s='cell (%d, %d)' % (row, col))

class App(wx.App):

    def OnInit(self):
        frame = Frame()
        frame.Show()
        self.SetTopWindow(frame)
        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()




