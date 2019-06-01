#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Bitmap ComboBox.
#-----------------------------------------------------------------------------

import wx
import wx.combo

class Frame(wx.Frame):

    def __init__(self, parent=None, id=-1):
        super(self.__class__, self).__init__(parent=parent, id=id, title='Bitmap ComboBox')
        panel = wx.Panel(parent=self, id=-1)

        bcb = wx.combo.BitmapComboBox(parent=panel, size=(200, -1))
        self.Bind(event=wx.EVT_COMBOBOX, handler=self.OnBcb, source=bcb)

        # colorList = ('Blue', 'Green', 'Red', 'Cyan', 'Magenta', 'Yellow', 'Black')

        colorList = ('aquamarine', 'black', 'blue', 'blue violet', 'brown', 'cadet blue', 'coral', 'cornflower blue', 'cyan',
                     'dark gray', 'dark green', 'dark olive green', 'dark orchid', 'dark slate blue', 'dark slate gray',
                     'dark turquoise', 'dim gray', 'firebrick', 'forest green', 'gold', 'goldenrod', 'gray', 'green',
                     'green yellow', 'indian red', 'khaki', 'light blue', 'light gray', 'light steel blue', 'lime green',
                     'magenta', 'maroon', 'medium aquamarine','medium blue', 'medium forest green', 'medium goldenrod',
                     'medium orchid', 'medium sea green', 'medium slate blue', 'medium spring green', 'medium turquoise',
                     'medium violet red', 'midnight blue', 'navy', 'orange', 'orange red', 'orchid', 'pale green',
                     'pink', 'plum', 'purple', 'red', 'salmon', 'sea green', 'sienna', 'sky blue', 'slate blue', 'spring green',
                     'steel blue', 'tan', 'thistle', 'turquoise', 'violet', 'violet red', 'wheat', 'white', 'yellow', 'yellow green')

        for eachColor in colorList:
            bmp = self.MakeBitmap(eachColor)
            bcb.Append(item=eachColor, bitmap=bmp, clientData=eachColor)

        # layout
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(item=bcb, proportion=0, flag=wx.ALL, border=50)
        panel.SetSizer(mainSizer)
        mainSizer.SetSizeHints(self)
        self.CenterOnScreen()

    def MakeBitmap(self, color):
        bmp = wx.EmptyBitmap(20, 20)
        dc = wx.MemoryDC()
        dc.SelectObject(bmp)
        dc.SetBackground(wx.Brush(color))
        dc.Clear()
        dc.SelectObject(wx.NullBitmap)
        return bmp

    def OnBcb(self, event):
        print 'Now, get color: %s' % event.GetString()

class App(wx.App):

    def OnInit(self):
        frame = Frame()
        frame.Show()
        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()


