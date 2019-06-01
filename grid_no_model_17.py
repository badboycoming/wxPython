#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Simple grid.
#-----------------------------------------------------------------------------

import wx
import wx.grid

class SimpleGrid(wx.grid.Grid):

    def __init__(self, parent=None, id=-1):
        super(self.__class__, self).__init__(parent=parent, id=id)
        self.CreateGrid(numRows=15, numCols=8)

        self.SetColLabelValue(0, 'First')  # NOTE, cannot use keyword, due to not proper key word name in definition
        self.SetColLabelValue(1, 'Last')   # SetColLabelValue(self, int col, String ?)

        self.SetRowLabelValue(0, 'A')  # SetRowLabelValue(self, int row, String ?)
        self.SetRowLabelValue(1, 'B')
        self.SetRowLabelValue(2, 'C')
        self.SetRowLabelValue(3, 'D')
        self.SetRowLabelValue(4, 'E')
        self.SetRowLabelValue(5, 'F')
        self.SetRowLabelValue(6, 'G')
        self.SetRowLabelValue(7, 'H')
        self.SetRowLabelValue(8, 'I')

        self.SetCellValue(row=0, col=0, s='Li')  # SetCellValue(self, int row, int col, String s)
        self.SetCellValue(row=0, col=1, s='Lei')
        self.SetCellValue(row=1, col=0, s='Han')
        self.SetCellValue(row=1, col=1, s='Meimei')
        self.SetCellValue(row=2, col=0, s='Jim')
        self.SetCellValue(row=2, col=1, s='Green')
        self.SetCellValue(row=3, col=0, s='Li')
        self.SetCellValue(row=3, col=1, s='Li')
        self.SetCellValue(row=4, col=0, s='Lucy')
        self.SetCellValue(row=4, col=1, s='Li')
        self.SetCellValue(row=5, col=0, s='Lin')
        self.SetCellValue(row=5, col=1, s='Tao')
        self.SetCellValue(row=6, col=0, s='Uncle')
        self.SetCellValue(row=6, col=1, s='Wang')
        self.SetCellValue(row=7, col=0, s='Poly')
        self.SetCellValue(row=7, col=1, s='Bird')
        self.SetCellValue(row=8, col=0, s='Miss')
        self.SetCellValue(row=8, col=1, s='Gao')

#-----------------------------------------------------------------------------

class Frame(wx.Frame):

    def __init__(self, parent=None, id=-1):
        super(self.__class__, self).__init__(parent=parent, id=id, title='Grid', size=(800, 500))
        grid = SimpleGrid(parent=self, id=-1)

        self.CenterOnScreen()

class App(wx.App):

    def OnInit(self):
        self.frame = Frame()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()




