#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Bad example, chaose.
#-----------------------------------------------------------------------------

import wx

class Frame(wx.Frame):

    def __init__(self, parent=None, id=-1):
        super(self.__class__, self).__init__(parent=parent, id=id, title='Chaose', style=wx.DEFAULT_FRAME_STYLE^wx.MAXIMIZE_BOX^wx.RESIZE_BORDER)

        panel = wx.Panel(parent=self)
        panel.SetBackgroundColour('White')

        #############
        # Add Button
        firstBtn = wx.Button(parent=panel, id=-1, label='FIRST')
        self.Bind(event=wx.EVT_BUTTON, handler=self.OnFirst, source=firstBtn)

        prevBtn = wx.Button(parent=panel, id=-1, label='<< PREV')
        self.Bind(event=wx.EVT_BUTTON, handler=self.OnPrev, source=prevBtn)

        nextBtn = wx.Button(parent=panel, id=-1, label='NEXT >>')
        self.Bind(event=wx.EVT_BUTTON, handler=self.OnNext, source=nextBtn)

        lastBtn = wx.Button(parent=panel, id=-1, label='LAST')
        self.Bind(event=wx.EVT_BUTTON, handler=self.OnLast, source=lastBtn)

        # Button layout
        buttonSizer = wx.BoxSizer(wx.HORIZONTAL)
        buttonSizer.Add(item=firstBtn, proportion=0, flag=wx.ALL, border=5)
        buttonSizer.Add(item=prevBtn, proportion=0, flag=wx.ALL^wx.LEFT, border=5)
        buttonSizer.Add(item=nextBtn, proportion=0, flag=wx.ALL^wx.LEFT, border=5)
        buttonSizer.Add(item=lastBtn, proportion=0, flag=wx.ALL^wx.LEFT, border=5)

        ###########
        # Add Menu
        menuFile = wx.Menu()
        open = menuFile.Append(id=-1, text='&Open', help='Open a item')
        self.Bind(event=wx.EVT_MENU, handler=self.OnOpen, source=open)
        menuFile.AppendSeparator()
        exit = menuFile.Append(id=-1, text='E&xit', help='Exit the GUI')
        self.Bind(event=wx.EVT_MENU, handler=self.OnCloseWindow, source=exit)

        menuEdit = wx.Menu()
        copy = menuEdit.Append(id=-1, text='&Copy', help='Copy an item')
        self.Bind(event=wx.EVT_MENU, handler=self.OnCopy, source=copy)
        cut = menuEdit.Append(id=-1, text='C&ut', help='Cut an item')
        self.Bind(event=wx.EVT_MENU, handler=self.OnCut, source=cut)
        paste = menuEdit.Append(id=-1, text='&Paste', help='Paste an item')
        self.Bind(event=wx.EVT_MENU, handler=self.OnPaste, source=paste)
        menuEdit.AppendSeparator()
        opt = menuEdit.Append(id=-1, text='&Options...', help='Display Options')
        self.Bind(event=wx.EVT_MENU, handler=self.OnOptions, source=opt)

        mb = wx.MenuBar()
        mb.Append(menu=menuFile, title='&File')
        mb.Append(menu=menuEdit, title='&Edit')
        self.SetMenuBar(menubar=mb)

        ################
        # Add status bar
        sb = self.CreateStatusBar()
        self.SetStatusBar(statBar=sb)

        #############################
        # Add static text & text ctrl
        st1 = wx.StaticText(parent=panel, id=-1, label='First Name')
        txt1 = wx.TextCtrl(parent=panel, id=-1, value='', size=(100, -1))

        st2 = wx.StaticText(parent=panel, id=-1, label='Last Name')
        txt2 = wx.TextCtrl(parent=panel, id=-1, value='', size=(100, -1))

        # static text & text ctrl layout
        stcSizer = wx.FlexGridSizer(rows=2, cols=2, hgap=5, vgap=5)
        stcSizer.Add(item=st1, proportion=0, flag=wx.ALIGN_CENTER_VERTICAL)
        stcSizer.Add(item=txt1, proportion=0)
        stcSizer.Add(item=st2, proportion=0, flag=wx.ALIGN_CENTER_VERTICAL)
        stcSizer.Add(item=txt2, proportion=0)

        ##############
        # Frame layout
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(item=buttonSizer, proportion=0)
        mainSizer.Add(item=stcSizer, proportion=0, flag=wx.TOP|wx.BOTTOM|wx.ALIGN_CENTER, border=20)
        # self.SetSizer(mainSizer)   #### why ?
        panel.SetSizer(mainSizer)
        # mainSizer.Fit(self)
        mainSizer.SetSizeHints(self)
        self.CenterOnScreen()

        #############
        # Frame close
        self.Bind(event=wx.EVT_CLOSE, handler=self.OnCloseWindow)

    ################
    # Button handler
    def OnFirst(self, event): pass
    def OnPrev(self, event): pass
    def OnNext(self, event): pass
    def OnLast(self, event): pass
    def OnCloseWindow(self, event):
        # self.Close()  #### why, due to Frame.Close() generate wx.EVT_CLOSE, so ... endless loop ... failed with maximun recursion reach
        self.Destroy()
    def OnOpen(self, event): pass
    def OnCopy(self, event): pass
    def OnPaste(self, event): pass
    def OnCut(self, event): pass
    def OnOptions(self, event): pass

class App(wx.App):

    def OnInit(self):
        self.frame = Frame()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()



