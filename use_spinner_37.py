#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: To demo how to use spinner.
#-----------------------------------------------------------------------------

import wx

class SpinnerFrame(wx.Frame):
    
    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='Spinner')
        panel = wx.Panel(parent=self, id=-1)

        # for integer spinner
        sc = wx.SpinCtrl(parent=panel, id=-1, value='', size=(80, -1))
        sc.SetRange(minVal=0, maxVal=100)
        sc.SetValue(15)

        # for float spinner
        scd = wx.SpinCtrlDouble(parent=panel, id=-1, size=(80, -1), inc=0.001)
        scd.SetRange(minVal=0, maxVal=10)
        scd.SetValue(1.002)
        # scd.SetIncrement = 0.01

        # layout
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(item=sc, proportion=0, flag=wx.CENTER|wx.ALL, border=50)
        mainSizer.Add(item=scd, proportion=0, flag=wx.CENTER|wx.ALL^wx.TOP, border=50)

        panel.SetSizer(mainSizer)
        mainSizer.SetSizeHints(self)
        self.CenterOnScreen()

class SpinnerApp(wx.App):
    
    def OnInit(self):
        self.frame = SpinnerFrame()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True
    
if __name__ == '__main__':
    
    app = SpinnerApp()
    app.MainLoop()
    
    

