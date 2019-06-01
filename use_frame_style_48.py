#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Use frame style.
#-----------------------------------------------------------------------------

import wx

class Frame(wx.Frame):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='Frame Style', size=(500, 300),
                                             # style=wx.DEFAULT_FRAME_STYLE
                                             # style=wx.DEFAULT_FRAME_STYLE | wx.FRAME_NO_TASKBAR   # window not display in taskbar
                                             # style=wx.DEFAULT_FRAME_STYLE | wx.FRAME_SHAPED       # maybe non-rectangular window
                                             # style=wx.DEFAULT_FRAME_STYLE | wx.FRAME_TOOL_WINDOW  # tool window, not display in taskbar
                                             # style=wx.DEFAULT_FRAME_STYLE | wx.ICONIZE            # minimize when create
                                             # style=wx.DEFAULT_FRAME_STYLE | wx.MINIMIZE           # minimize when create, same as above
                                             # style=wx.DEFAULT_FRAME_STYLE | wx.MAXIMIZE           # maximize when create

                                             style=wx.FRAME_TOOL_WINDOW | wx.CAPTION | wx.SYSTEM_MENU | wx.CLOSE_BOX  # tool window, simplify

                                             # style=wx.DEFAULT_FRAME_STYLE ^ wx.MAXIMIZE_BOX  # NOTE, the system menu will not contain max box item
                                             # style=wx.DEFAULT_FRAME_STYLE ^ (wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX)
                                             )
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



