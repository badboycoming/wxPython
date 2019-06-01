#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: To demo how to use slider.
#-----------------------------------------------------------------------------

import wx

class SliderFrame(wx.Frame):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='Silder')
        panel = wx.Panel(parent=self, id=-1)

        sliderH = wx.Slider(parent=panel, id=-1, value=25, minValue=0, maxValue=100, size=(250, -1),
                           style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS | wx.SL_LABELS)
        sliderH.SetTickFreq(5, 1)

        sliderV = wx.Slider(parent=panel, id=-1, value=20, minValue=0, maxValue=100, size=(-1, 250),
                           style=wx.SL_VERTICAL | wx.SL_AUTOTICKS | wx.SL_LABELS)
        sliderV.SetTickFreq(10, 1)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(item=sliderH, proportion=0, flag=wx.ALL, border=10)
        mainSizer.Add(item=sliderV, proportion=0, flag=wx.CENTER|wx.ALL, border=10)

        panel.SetSizer(mainSizer)
        mainSizer.SetSizeHints(self)
        self.CenterOnScreen()

class SliderApp(wx.App):
    
    def OnInit(self):
        self.frame = SliderFrame()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True
    
if __name__ == '__main__':
    
    app = SliderApp()
    app.MainLoop()
    

