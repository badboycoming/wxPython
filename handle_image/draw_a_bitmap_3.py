#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Draw a bitmap.
#-----------------------------------------------------------------------------

import wx
import random
random.seed()

class RandomImagePlacementWindow(wx.Window):

    def __init__(self, parent, image):
        super(self.__class__, self).__init__(parent=parent)
        self.photo = image.ConvertToBitmap()

        self.positions = [(10, 10)]
        for x in range(50):
            x = random.randint(0, 1920)
            y = random.randint(0, 1080)
            self.positions.append((x, y))

        self.Bind(event=wx.EVT_PAINT, handler=self.OnPaint)

    def OnPaint(self, event):
        dc = wx.PaintDC(win=self)
        brush = wx.Brush(colour='sky blue')
        dc.SetBackground(brush=brush)
        dc.Clear()  # clear the DC with background brush

        for x, y in self.positions:
            dc.DrawBitmap(bmp=self.photo, x=x, y=y, useMask=True)

#-----------------------------------------------------------------------------

class Frame(wx.Frame):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, title='Load Images', size=(640, 480))
        img = wx.Image('sun.png')
        img.SetMaskColour(r=255, g=255, b=255)  # set white color to mask
        RandomImagePlacementWindow(parent=self, image=img)

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



