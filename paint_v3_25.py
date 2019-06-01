#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: paint version 3, add status, more regions.
#-----------------------------------------------------------------------------

import wx
from paint_v1_23 import SketchWindow

class Frame(wx.Frame):

    def __init__(self, parent=None, id=-1):
        super(self.__class__, self).__init__(parent=parent, id=id, title='Paint', size=(800, 600))
        self.sketch = SketchWindow(parent=self, id=-1)

        self.sketch.Bind(event=wx.EVT_MOTION, handler=self.OnSketchMotion)

        self.sb = self.CreateStatusBar()
        self.sb.SetFieldsCount(3)
        self.sb.SetStatusWidths([-1, -2, -3])
        self.SetStatusBar(statBar=self.sb)

        self.CenterOnScreen()

    def OnSketchMotion(self, event):
        self.sb.SetStatusText(text='Pos: %s' % str(event.GetPositionTuple()), number=0)
        self.sb.SetStatusText(text='Current Pts: %s' % len(self.sketch.curLine), number=1)
        self.sb.SetStatusText(text='Line Cnts: %s' % len(self.sketch.lines), number=2)
        event.Skip()

class App(wx.App):

    def OnInit(self):
        self.frame = Frame()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()





