#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Simple grid, build with abstract class PyGridTableBase.
#-----------------------------------------------------------------------------

import wx
import wx.grid

class SchoolMemberTable(wx.grid.PyGridTableBase):  # NOTE, base class is a ADT, should re-define its' methods in derive class.

    data = (
        ('A', 'Li', 'Lei'),
        ('B', 'Han', 'Meimei'),
        ('C', 'Jim', 'Green'),
        ('D', 'Li', 'Li'),
        ('E', 'Lucy', 'Li'),
        ('F', 'Lin', 'Tao'),
        ('G', 'Uncle', 'Wang'),
        ('H', 'Poly', 'Brid'),
        ('I', 'Miss', 'Gao'),
    )
    colLabels = ('First', 'Last')

    def __init__(self):
        super(self.__class__, self).__init__()

    def GetNumberRows(self):
        return len(self.data)

    def GetNumberCols(self):
        return len(self.colLabels)

    def IsEmptyCell(self, row, col):
        return False  # here stub

    def GetValue(self, row, col):
        return self.data[row][col+1]

    def SetValue(self, row, col, value):
        pass  # here stub

    def GetRowLabelValue(self, row):
        return self.data[row][0]

    def GetColLabelValue(self, col):
        return self.colLabels[col]

class SimpleGrid(wx.grid.Grid):
    def __init__(self, parent=None, id=-1):
        super(self.__class__, self).__init__(parent=parent, id=id)
        self.SetTable(table=SchoolMemberTable())

#-----------------------------------------------------------------------------

class Frame(wx.Frame):
    def __init__(self, parent=None, id=-1):
        super(self.__class__, self).__init__(parent=parent, id=id, title='Grid', size=(800, 500))
        grid = SimpleGrid(parent=self)

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



