#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Grid use GenericTable.
#-----------------------------------------------------------------------------

import wx
import wx.grid
import GenericTable
# import pdb; pdb.set_trace()

class SimpleGrid(wx.grid.Grid):
    def __init__(self, parent=None, id=-1):
        super(self.__class__, self).__init__(parent=parent, id=id)

        data = (
            ('Li', 'Lei'),
            ('Han', 'Meimei'),
            ('Li', 'Li'),
            ('Lucy', 'Li'),
            ('Jim', 'Green'),
            ('Lin', 'Tao'),
            ('Uncle', 'Wang'),
            ('Poly', 'Bird'),
            ('Miss', 'Gao'),
        )
        colLabels = ('First', 'Last')
        rowLabels = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I')

        tableBase = GenericTable.GenericTable(data=data, rowLabels=rowLabels, colLabels=colLabels)
        self.SetTable(table=tableBase)

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



