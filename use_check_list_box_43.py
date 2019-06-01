#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: To demo how to use check list box.
#-----------------------------------------------------------------------------

import wx

class CheckListBoxFrame(wx.Frame):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='Check List Box')
        panel = wx.Panel(parent=self, id=-1)

        sampleList = ['zero', 'one', 'two', 'three', 'four', 'five', 'six',
                      'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
                      'thirteen', 'fourteen']
        # clb = wx.CheckListBox(parent=panel, id=-1, size=(100, 120), choices=sampleList, style=wx.LB_SINGLE)
        clb = wx.CheckListBox(parent=panel, id=-1, size=(-1, -1), choices=sampleList, style=wx.LB_SINGLE)
        clb.Check(3, True)

        # layout
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(item=clb, proportion=0, flag=wx.ALL, border=30)
        panel.SetSizer(mainSizer)
        mainSizer.SetSizeHints(self)
        self.CenterOnScreen()

class CheckListBoxApp(wx.App):

    def OnInit(self):
        frame = CheckListBoxFrame()
        frame.Show()
        self.SetTopWindow(frame)
        return True

if __name__ == '__main__':

    app = CheckListBoxApp()
    app.MainLoop()




