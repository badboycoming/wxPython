#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Grid.
#-----------------------------------------------------------------------------

import wx
import wx.grid

class TableEntry(object):

    def __init__(self, rowLabel, col1st, col2nd):
        self.rowLabel = rowLabel
        self.col1st = col1st
        self.col2nd= col2nd

class GridTable(wx.grid.PyGridTableBase):

    colLabels = ('First', 'Last')
    colAttrs = ('col1st', 'col2nd')

    def __init__(self, entries):
        super(self.__class__, self).__init__()
        self.entries = entries

    def GetNumberRows(self):
        return len(self.entries)

    def GetNumberCols(self):
        return len(self.colLabels)

    def GetColLabelValue(self, col):
        return self.colLabels[col]

    def GetRowLabelValue(self, row):
        return self.entries[row].rowLabel

    def IsEmptyCell(self, row, col):
        return False  # here stub

    def GetValue(self, row, col):
        entry = self.entries[row]
        return getattr(entry, self.colAttrs[col])

    def SetValue(self, row, col, value):
        pass  # here stub

#-----------------------------------------------------------------------------

class SimpleGrid(wx.grid.Grid):
    def __init__(self, parent=None, id=-1):
        super(self.__class__, self).__init__(parent=parent, id=id)
        entries = (
            TableEntry('A', 'Li', 'Lei'),
            TableEntry('B', 'Han', 'Meimei'),
            TableEntry('C', 'Jim', 'Green'),
            TableEntry('D', 'Li', 'Li'),
            TableEntry('E', 'Lucy', 'Li'),
            TableEntry('F', 'Lin', 'Tao'),
            TableEntry('G', 'Uncle', 'Wang'),
            TableEntry('H', 'Poly', 'Bird'),
            TableEntry('I', 'Miss', 'Gao'),
        )
        table = GridTable(entries=entries)
        self.SetTable(table=table)

#-----------------------------------------------------------------------------

class Frame(wx.Frame):
    def __init__(self, parent=None, id=-1):
        super(self.__class__, self).__init__(parent=parent, id=id, title='Grid', size=(800, 500))
        grid = SimpleGrid(parent=self)

class App(wx.App):
    def OnInit(self):
        self.frame = Frame()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':
    app = App()
    app.MainLoop()



