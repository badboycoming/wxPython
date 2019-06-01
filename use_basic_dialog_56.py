#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Use basic dialog.
#-----------------------------------------------------------------------------

import wx

class Dialog(wx.Dialog):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='Dialog')

        okBtn = wx.Button(parent=self, id=wx.ID_OK, label='OK')
        cancelBtn = wx.Button(parent=self, id=wx.ID_CANCEL, label='Cancel')
        cancelBtn.SetDefault()  # seems set default have no effect under MS-Windows

        # layout
        subSizer = wx.BoxSizer(wx.HORIZONTAL)
        subSizer.Add(item=okBtn, proportion=0, flag=wx.ALL, border=5)
        subSizer.Add(item=cancelBtn, proportion=0, flag=wx.ALL^wx.LEFT, border=5)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(item=subSizer, proportion=0, flag=wx.ALL, border=30)
        self.SetSizer(mainSizer)
        mainSizer.SetSizeHints(self)
        self.CenterOnScreen()

class App(wx.App):

    def OnInit(self):
        dialog = Dialog()
        rtv = dialog.ShowModal()
        if rtv == wx.ID_OK:
            print 'OK'
        else:
            print 'Cancel'
        dialog.Destroy()
        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()


