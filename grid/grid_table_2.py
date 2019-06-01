#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Grid table. Use drive of "wx.grid.PyGridTableBase" and "SetTable" to create.
#-----------------------------------------------------------------------------

import wx
import wx.grid

class TestTable(wx.grid.PyGridTableBase):

    def __init__(self):
        super(self.__class__, self).__init__()

        self.data = {(1, 1) : 'Here',
                     (2, 2) : 'is',
                     (3, 3) : 'some',
                     (4, 4) : 'data',}

        self.odd = wx.grid.GridCellAttr()
        self.odd.SetBackgroundColour('sky blue')
        self.odd.SetFont(wx.Font(pointSize=10, family=wx.MODERN, style=wx.NORMAL, weight=wx.NORMAL, faceName=u'宋体'))

        self.even = wx.grid.GridCellAttr()
        self.even.SetBackgroundColour('light gray')
        self.even.SetFont(wx.Font(pointSize=9, family=wx.MODERN, style=wx.NORMAL, weight=wx.NORMAL, faceName='Consolas'))

    def GetNumberRows(self):
        return 50

    def GetNumberCols(self):
        return 50

    def IsEmptyCell(self, row, col):
        return self.data.get((row, col)) is not None

    def GetValue(self, row, col):
        value = self.data.get((row, col))
        if value is not None:
            return value
        else:
            return ''

    def SetValue(self, row, col, value):
        self.data[(row, col)] = value

    def GetAttr(self, row, col, kind):
        attr = [self.even, self.odd][row % 2]
        attr.IncRef()
        return attr

#-----------------------------------------------------------------------------

class Frame(wx.Frame):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, title='Grid Table', size=(700, 500))

        grid = wx.grid.Grid(parent=self)
        grid.SetTable(table=TestTable(), takeOwnership=True)

class App(wx.App):

    def OnInit(self):
        frame = Frame()
        frame.Show()
        self.SetTopWindow(frame)
        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()







