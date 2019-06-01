#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: load and scale image.
#-----------------------------------------------------------------------------

import wx

filenames = ['image.bmp', 'image.gif', 'image.jpg', 'image.png']

class Frame(wx.Frame):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, title='Load & Handle Image')
        panel = wx.Panel(parent=self)

        fgsizer = wx.FlexGridSizer(cols=2, hgap=10, vgap=10)
        for item in filenames:
            img1 = wx.Image(name=item, type=wx.BITMAP_TYPE_ANY)
            wid = img1.GetWidth()
            hig = img1.GetHeight()
            img2 = img1.Scale(width=wid/2, height=hig/2, quality=wx.IMAGE_QUALITY_NORMAL)
            # img2 = img1.Scale(width=wid/2, height=hig/2, quality=wx.IMAGE_QUALITY_HIGH)

            sb1 = wx.StaticBitmap(parent=panel, id=-1, bitmap=wx.BitmapFromImage(img1))
            sb2 = wx.StaticBitmap(parent=panel, id=-1, bitmap=wx.BitmapFromImage(img2))

            fgsizer.Add(item=sb1, flag=wx.ALL, border=10)
            fgsizer.Add(item=sb2, flag=wx.ALL, border=10)

        # panel.SetSizerAndFit(fgsizer)
        panel.SetSizer(fgsizer)
        fgsizer.Fit(self)

        self.CenterOnScreen()

class App(wx.App):

    def OnInit(self):
        frame = Frame()
        frame.Show()
        self.SetTopWindow(frame)
        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()




