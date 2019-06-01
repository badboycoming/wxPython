#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Set grid row & column header. (default is 1, 2, 3, ... and A, B, C, ...)
#-----------------------------------------------------------------------------

import wx
import wx.grid

class TestTable(wx.grid.PyGridTableBase):

    def __init__(self):
        super(self.__class__, self).__init__()

        self.rowLabels = ['one', 'two', 'three', 'four', 'five']
        self.colLabels = ['1st', '2nd', '3rd', '4th', '5th']

    def GetNumberRows(self):
        return 5

    def GetNumberCols(self):
        return 5

    def IsEmptyCell(self, row, col):
        return False

    def GetValue(self, row, col):
        return '(%s, %s)' % (self.rowLabels[row], self.colLabels[col])

    def SetValue(self, row, col, value):
        pass

    def GetColLabelValue(self, col):  # col label, no need Set, set is auto
        return self.colLabels[col]

    def GetRowLabelValue(self, row):  # row label, no need Set, set is auto
        return self.rowLabels[row]

#-----------------------------------------------------------------------------

class Frame(wx.Frame):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, title='Grid Table', size=(700, 500))

        g = wx.grid.Grid(parent=self)
        g.SetTable(table=TestTable(), takeOwnership=True)

class App(wx.App):

    def OnInit(self):
        frame = Frame()
        frame.Show()
        self.SetTopWindow(frame)
        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()







