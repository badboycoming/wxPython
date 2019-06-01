#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: To demo how to use bitmap button.
#-----------------------------------------------------------------------------

import wx

class BitmapButtonFrame(wx.Frame):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='Bitmap Button')
        panel = wx.Panel(parent=self, id=-1)
        bmp = wx.Image(name='./bitmap.bmp', type=wx.BITMAP_TYPE_BMP).ConvertToBitmap()

        btn = wx.BitmapButton(parent=panel, id=-1, bitmap=bmp)
        self.Bind(event=wx.EVT_BUTTON, handler=self.OnClick, source=btn)
        # btn.SetDefault()  # seems no effect

        btn2 = wx.BitmapButton(parent=panel, id=-1, bitmap=bmp)
        self.Bind(event=wx.EVT_BUTTON, handler=self.OnClick2, source=btn2)
        # btn2.SetDefault()  # seems no effect

        subSizer = wx.BoxSizer(wx.HORIZONTAL)
        subSizer.Add(item=btn, proportion=0, flag=wx.ALL, border=5)
        subSizer.Add(item=btn2, proportion=0, flag=wx.ALL, border=5)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(item=subSizer, proportion=0, flag=wx.CENTER|wx.ALL, border=50)

        panel.SetSizer(mainSizer)
        mainSizer.SetSizeHints(self)
        # self.Center(wx.BOTH)
        self.CenterOnScreen()

    def OnClick(self, event):
        self.Destroy()

    def OnClick2(self, event):
        msg_dlg = wx.MessageDialog(parent=None, message='Hello!', caption='MessageDialog', style=wx.OK)
        msg_dlg.ShowModal()
        msg_dlg.Destroy()

class BitmapButtonApp(wx.App):

    def OnInit(self):
        self.frame = BitmapButtonFrame()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':

    app = BitmapButtonApp()
    app.MainLoop()





