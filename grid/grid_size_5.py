#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Grid size.
#-----------------------------------------------------------------------------

import wx
import wx.grid

class Frame(wx.Frame):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, title='Grid Size', size=(700, 500))

        g = wx.grid.Grid(parent=self)
        g.CreateGrid(numRows=5, numCols=5)

        for row in range(5):
            for col in range(5):
                g.SetCellValue(row=row, col=col, s='(%s, %s)' % (row, col))

        ##################
        # Adjust grid size
        ##################
        # g.SetCellSize(row=2, col=2, num_rows=2, num_cols=3)  # grid span across rows and cols

        # g.SetColSize(col=1, width=150)  # widht in pixels
        # g.SetRowSize(row=4, height=50)  # height in pixels

        # g.SetDefaultColSize(width=100, resizeExistingCols=False)
        # g.SetDefaultRowSize(height=100, resizeExistingRows=False)

        # g.SetColMinimalAcceptableWidth(width=100)
        # g.SetRowMinimalAcceptableHeight(width=20)

        g.SetCellValue(row=2, col=1, s='This is a long cell test.')
        g.SetCellValue(row=3, col=4, s='This is a long cell test.')
        g.SetCellValue(row=4, col=1, s='This is a long \ncell test.')
        g.AutoSize()

class App(wx.App):

    def OnInit(self):
        frame = Frame()
        frame.Show()
        self.SetTopWindow(frame)
        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()



