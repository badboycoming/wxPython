#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Generic Table, from PyGridTableBase.
#-----------------------------------------------------------------------------

import wx
import wx.grid

class GenericTable(wx.grid.PyGridTableBase):

    def __init__(self, data, rowLabels=None, colLabels=None):
        super(self.__class__, self).__init__()
        self.data = data
        self.rowLabels = rowLabels
        self.colLabels = colLabels

    def GetNumberRows(self):
        return len(self.data)

    def GetNumberCols(self):
        return len(self.data[0])

    def IsEmpty(self):
        return False  # here stub

    def GetValue(self, row, col):
        return self.data[row][col]

    def SetValue(self, row, col, val):
        pass  # here stub

    def GetColLabelValue(self, col):
        if self.colLabels:
            return self.colLabels[col]

    def GetRowLabelValue(self, row):
        if self.rowLabels:
            return self.rowLabels[row]





