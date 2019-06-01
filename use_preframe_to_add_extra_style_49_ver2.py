#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Use PreFrame to add extra style, version 2. Not easy to understand
#-----------------------------------------------------------------------------

import wx

def twoStepCreate(instance, preClass, preInitFunc, *args, **kwargs):
    pre = preClass()
    preInitFunc(pre)
    pre.Create(*args, **kwargs)
    instance.PostCreate(pre)

class Frame(wx.Frame):

    # def __init__(self, parent=None, id=-1, title='Help context', size=(500, 300)):     #### seems the following style no use
    #     twoStepCreate(instance=self, preClass=wx.PreFrame, preInitFunc=self.preInit,
    #                   parent=parent, id=id, title=title, size=size)

    # def __init__(self, parent=None, id=-1, title='Help context', size=(500, 300), style=wx.DEFAULT_FRAME_STYLE ^ (wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX)):
    #     twoStepCreate(instance=self, preClass=wx.PreFrame, preInitFunc=self.preInit,
    #                   parent=parent, id=id, title=title, size=size, style=style)

    def __init__(self, parent=None, id=-1, title='Help context', size=(500, 300), style=wx.DEFAULT_DIALOG_STYLE):
        twoStepCreate(instance=self, preClass=wx.PreFrame, preInitFunc=self.preInit,
                      parent=parent, id=id, title=title, size=size, style=style)
        self.CenterOnScreen()

    def preInit(self, pre):
        pre.SetExtraStyle(wx.FRAME_EX_CONTEXTHELP)

class App(wx.App):

    def OnInit(self):
        frame = Frame()
        frame.Show()
        self.SetTopWindow(frame)
        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()




