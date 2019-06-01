#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: To demo how to use list box.
#-----------------------------------------------------------------------------

import wx

class ListBoxFrame(wx.Frame):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='List Box')
        panel = wx.Panel(parent=self, id=-1)

        sampleList = ['zero', 'one', 'two', 'three', 'four', 'five', 'six',
                      'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
                      'thirteen', 'fourteen']
        listBox = wx.ListBox(parent=panel, id=-1, size=(100, 120), choices=sampleList, style=wx.LB_SINGLE)
        # listBox = wx.ListBox(parent=panel, id=-1, size=(-1, -1), choices=sampleList, style=wx.LB_SINGLE)
        listBox.SetSelection(3)

        # layout
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(item=listBox, proportion=0, flag=wx.ALL, border=30)
        panel.SetSizer(mainSizer)
        mainSizer.SetSizeHints(self)
        # self.Center(wx.BOTH)
        self.CenterOnScreen()


class ListBoxApp(wx.App):

    def OnInit(self):
        frame = ListBoxFrame()
        frame.Show()
        self.SetTopWindow(frame)
        return True

if __name__ =='__main__':

    app = ListBoxApp()
    app.MainLoop()







