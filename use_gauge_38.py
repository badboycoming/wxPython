#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: To demo how to use gauge.
#-----------------------------------------------------------------------------

import wx
import time

class GaugeFrame(wx.Frame):
    
    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='Gauge')
        panel = wx.Panel(parent=self, id=-1)
        
        self.gauge = wx.Gauge(parent=panel, id=-1, range=300, size=wx.DefaultSize, style=wx.GA_PROGRESSBAR)
        # self.gauge.SetBezelFace(3)
        # self.gauge.SetShadowWidth(3)
        self.Bind(event=wx.EVT_IDLE, handler=self.OnIdle)
        self.cnt = 0

        # layout
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(item=self.gauge, proportion=0, flag=wx.CENTER|wx.ALL, border=30)

        panel.SetSizer(mainSizer)
        mainSizer.SetSizeHints(self)
        self.CenterOnScreen()

        
    def OnIdle(self, event):
        self.cnt += 1
        self.gauge.SetValue(self.cnt)
        if self.cnt == 300:
            print '+++ Well Done +++'  # for test

class GaugeApp(wx.App):
    
    def OnInit(self):
        self.frame = GaugeFrame()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True
    
if __name__ == '__main__':
    
    app = GaugeApp()
    app.MainLoop()
    
    





