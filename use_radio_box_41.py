#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: To demo how to use radio box.
#-----------------------------------------------------------------------------

import wx

class RadioBoxFrame(wx.Frame):
    
    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='Radio Box')
        panel = wx.Panel(parent=self, id=-1)
        sampleList = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight']

        rb1 = wx.RadioBox(parent=panel, id=-1, label='A Radio Box', choices=sampleList, majorDimension=2, style=wx.RA_SPECIFY_COLS)
        rb2 = wx.RadioBox(parent=panel, id=-1, label='', choices=sampleList, majorDimension=3, style=wx.RA_SPECIFY_COLS)

        # layout
        subSizer = wx.BoxSizer(wx.HORIZONTAL)
        subSizer.Add(item=rb1, proportion=0, flag=wx.ALL, border=10)
        subSizer.Add(item=rb2, proportion=0, flag=wx.ALL^wx.LEFT, border=10)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(item=subSizer, proportion=0, flag=wx.ALL, border=30)
        panel.SetSizer(mainSizer)
        mainSizer.SetSizeHints(self)
        # self.Center(wx.BOTH)
        self.CenterOnScreen()
        
class RadioBoxApp(wx.App):
    
    def OnInit(self):
        self.frame = RadioBoxFrame()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True 
    
if __name__ == '__main__':
    
    app = RadioBoxApp()
    app.MainLoop()


