#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: To demo how to use checkbox.
#-----------------------------------------------------------------------------

import wx

class CheckBoxFrame(wx.Frame):
    
    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='CheckBox', size=(150, 200))
        panel = wx.Panel(parent=self, id=-1)
        
        alp = wx.CheckBox(parent=panel, id=-1, label='Alpha') #, pos=(35, 40))  #, size=(150, 20))
        bet = wx.CheckBox(parent=panel, id=-1, label='Beta') #, pos=(35, 60))  #, size=(150, 20))
        gam = wx.CheckBox(parent=panel, id=-1, label='Gamma') #, pos=(35, 80))  #, size=(150, 20))

        # layout
        textbox = wx.StaticBox(parent=panel, id=-1, label='Item')
        sizer = wx.StaticBoxSizer(box=textbox, orient=wx.VERTICAL)
        sizer.Add(item=alp, proportion=0, flag=wx.ALL, border=5)
        sizer.Add(item=bet, proportion=0, flag=wx.ALL^wx.TOP^wx.BOTTOM, border=5)
        sizer.Add(item=gam, proportion=0, flag=wx.ALL, border=5)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(item=sizer, proportion=0, flag=wx.ALL, border=40)

        panel.SetSizer(mainSizer)
        mainSizer.SetSizeHints(self)
        # self.Center(wx.BOTH)
        self.CenterOnScreen()


class CheckBoxApp(wx.App):
    
    def OnInit(self):
        self.frame = CheckBoxFrame()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True
    
if __name__ == '__main__':
    
    app = CheckBoxApp()
    app.MainLoop()
    
    
    