#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: To demo how to use static text.
#-----------------------------------------------------------------------------

import wx

class StaticTextFrame(wx.Frame):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='Static Text') #, size=(600, 300))
        panel = wx.Panel(parent=self, id=-1)

        mainSizer = wx.BoxSizer(wx.VERTICAL)

        #######
        # Basic
        #######

        st1 = wx.StaticText(parent=panel, id=-1, label='This is an example of static text')
        mainSizer.Add(item=st1, proportion=0, flag=wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, border=5)

        #####################
        # set fore/back color
        #####################

        st2 = wx.StaticText(parent=panel, id=-1, label='Static Text With Reversed Colors')
        st2.SetForegroundColour('white')
        st2.SetBackgroundColour('black')
        mainSizer.Add(item=st2, proportion=0, flag=wx.ALIGN_CENTER_HORIZONTAL)

        ## set style, due to using sizer, so following two have no effect
        # st3 = wx.StaticText(parent=panel, id=-1, label='Align Center Example', style=wx.ALIGN_CENTER)
        # st4 = wx.StaticText(parent=panel, id=-1, label='Align Right Exampel', style=wx.ALIGN_RIGHT)

        #############
        # change font
        #############

        text = 'You can also change the font.'
        st5 = wx.StaticText(parent=panel, id=-1, label=text)
        font = wx.Font(pointSize=18, family=wx.DECORATIVE, style=wx.ITALIC, weight=wx.NORMAL)
        st5.SetFont(font)
        mainSizer.Add(item=st5, proportion=0, flag=wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, border=5)

        ###########
        # multiline
        ###########

        subSizer = wx.BoxSizer(wx.HORIZONTAL)

        text2 = 'Your text\ncan be split\nover multiple lines\n\neven blank ones.'
        st6 = wx.StaticText(parent=panel, id=-1, label=text2)
        text3 = 'Multi-line text\ncan also\nbe right aligned\n\neven with a blank.'
        st7 = wx.StaticText(parent=panel, id=-1, label=text3, style=wx.ALIGN_RIGHT)

        subSizer.Add(item=st6, proportion=1, flag=wx.ALIGN_CENTER_HORIZONTAL|wx.RIGHT, border=20)
        subSizer.Add(item=st7, proportion=1, flag=wx.ALIGN_CENTER_HORIZONTAL|wx.LEFT, border=20)
        mainSizer.Add(item=subSizer, proportion=0, flag=wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, border=5)

        panel.SetSizer(mainSizer)
        mainSizer.SetSizeHints(self)
        self.CenterOnScreen()


class StaticTextApp(wx.App):

    def OnInit(self):
        self.frame = StaticTextFrame()
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

if __name__ == '__main__':

    app = StaticTextApp()
    app.MainLoop()





