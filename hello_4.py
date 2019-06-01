#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Purpose: To display an image.
#-------------------------------------------------------------------------------

import wx

class Frame(wx.Frame):

    def __init__(self, imageName, parent=None, id=-1, title='Hello, wxPython!'):

        bmp = wx.Image(name=imageName, type=wx.BITMAP_TYPE_JPEG).ConvertToBitmap()
        # bmpSize = bmp.GetWidth(), bmp.GetHeight()

        # super(self.__class__, self).__init__(parent=parent, id=id, title=title, size=bmpSize)
        super(self.__class__, self).__init__(parent=parent, id=id, title=title)
        self.bmp = wx.StaticBitmap(parent=self, bitmap=bmp)

        self.CenterOnScreen()
        # self.Fit()
        self.SetClientSize(self.bmp.GetSize())

class App(wx.App):

    def OnInit(self):
        frame = Frame(imageName='./wxPython.jpg')
        frame.Show()
        self.SetTopWindow(frame)
        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()




