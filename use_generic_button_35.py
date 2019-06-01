#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: To demo how to use generic button.
#-----------------------------------------------------------------------------

import wx
import wx.lib.buttons as buttons

class GenericButtonFrame(wx.Frame):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='Generic Button', size=(700, 350))
        panel = wx.Panel(parent=self, id=-1)

        gridSizer = wx.FlexGridSizer(rows=4, cols=3, vgap=20, hgap=20)

        ### row one
        b = wx.Button(parent=panel, id=-1, label='A common wx.Button')
        b.SetDefault()
        b.SetToolTipString('This is a common button...')
        gridSizer.Add(b)

        b = wx.Button(parent=panel, id=-1, label='non-default wx.Button')
        gridSizer.Add(b)

        gridSizer.Add((1, 1))  # add an empty space

        ### row two
        b = buttons.GenButton(parent=panel, id=-1, label='Generic Button')
        gridSizer.Add(b)

        b = buttons.GenButton(parent=panel, id=-1, label='Disable Generic Button')
        b.Enable(False)
        gridSizer.Add(b)

        b = buttons.GenButton(parent=panel, id=-1, label='bigger')
        b.SetFont(font=wx.Font(pointSize=20, family=wx.SWISS, style=wx.NORMAL, weight=wx.BOLD, underline=False))
        b.SetBezelWidth(5)
        b.SetBackgroundColour('Navy')
        b.SetForegroundColour('White')
        b.SetToolTipString('This is a Bit Button...')
        gridSizer.Add(b)

        ### row 3
        bmp = wx.Image(name='./bitmap.bmp', type=wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        b = buttons.GenBitmapButton(parent=panel, id=-1, bitmap=bmp)
        gridSizer.Add(b)

        b = buttons.GenBitmapToggleButton(parent=panel, id=-1, bitmap=bmp)
        gridSizer.Add(b)

        b = buttons.GenBitmapTextButton(parent=panel, id=-1, bitmap=bmp, label='Bitmapped Text', size=(175, 75))
        b.SetUseFocusIndicator(False)
        gridSizer.Add(b)

        ### row 4
        b = buttons.GenToggleButton(parent=panel, id=-1, label='Toggle Button')
        gridSizer.Add(b)

        ### layout
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(item=gridSizer, proportion=0, flag=wx.CENTER|wx.ALL, border=10)

        panel.SetSizer(mainSizer)
        mainSizer.SetSizeHints(self)
        self.CenterOnScreen()

class GenericButtonApp(wx.App):

    def OnInit(self):
        self.frame = GenericButtonFrame()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':

    app = GenericButtonApp()
    app.MainLoop()





