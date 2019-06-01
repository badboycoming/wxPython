#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Good example.
#-----------------------------------------------------------------------------

# import pdb; pdb.set_trace()
import wx

class Frame(wx.Frame):

    def __init__(self, parent=None, id=-1):
        super(self.__class__, self).__init__(parent=parent, id=id, title='Good', style=wx.DEFAULT_FRAME_STYLE^wx.MAXIMIZE_BOX^wx.RESIZE_BORDER)

        panel = wx.Panel(parent=self)
        panel.SetBackgroundColour('White')

        self._createMenuBar()
        btnSizer = self._createButtonGroup(parent=panel)
        stcSizer = self._createTextFields(parent=panel)

        self.Bind(event=wx.EVT_CLOSE, handler=self.OnCloseWindow)
        sb = self.CreateStatusBar()
        self.SetStatusBar(statBar=sb)

        ##############
        # Frame layout
        ##############
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(item=btnSizer, proportion=0, flag=wx.ALL^wx.RIGHT, border=5)
        mainSizer.Add(item=stcSizer, proportion=0, flag=wx.TOP|wx.BOTTOM|wx.ALIGN_CENTER, border=20)
        panel.SetSizer(mainSizer)
        mainSizer.SetSizeHints(self)
        self.CenterOnScreen()


    #--------------------------------------------------------------------------- Create Menu
    def menuData(self):  # for more elaborate application, the data can get from an xml file
        return (
            ('&File',
                ('&Open', 'Open an item', self.OnOpen),
                ('', '', ''),
                ('E&xit', 'Exit GUI', self.OnCloseWindow),
            ),
            ('&Edit',
                ('&Copy', 'Copy an item', self.OnCopy),
                ('C&ut', 'Cut an item', self.OnCut),
                ('&Paste', 'Paste an item', self.OnPaste),
                ('', '', ''),
                ('&Options...', 'Display an options', self.OnOption),
            ),
        )

    def __createMenu(self, menuItems):
        m = wx.Menu()
        for text, help, handler in menuItems:
            if text == '':
                m.AppendSeparator()
                continue
            mItem = m.Append(id=-1, text=text, help=help)
            self.Bind(event=wx.EVT_MENU, handler=handler, source=mItem)
        return m

    def _createMenuBar(self):
        mb = wx.MenuBar()
        for eachMenuData in self.menuData():
            menuTitle = eachMenuData[0]
            menuItems = eachMenuData[1:]
            mb.Append(menu=self.__createMenu(menuItems), title=menuTitle)
        self.SetMenuBar(menubar=mb)

    #------------------------------------------------------------------------- Create Button

    def _buttonData(self):
        return (
            ('FIRST', self.OnFirst),
            ('<< PREV', self.OnPrev),
            ('NEXT >>', self.OnNext),
            ('Last', self.OnLast),
        )

    def _buildOneButton(self, parent, label, handler):
        btn = wx.Button(parent=parent, id=-1, label=label)
        self.Bind(event=wx.EVT_BUTTON, handler=handler, source=btn)
        return btn

    def _createButtonGroup(self, parent):
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        for label, handler in self._buttonData():
            btn = self._buildOneButton(parent=parent, label=label, handler=handler)
            btnSizer.Add(item=btn, proportion=0, flag=wx.RIGHT, border=5)
        return btnSizer

    #------------------------------------------------------------------------- Create Textfields

    def _textFieldData(self):
        return (
            ('First Name'),
            ('Last Name'),
        )

    def _createTextFields(self, parent):
        data = self._textFieldData()
        stcSizer = wx.FlexGridSizer(rows=len(data), cols=2, hgap=5, vgap=5)
        for label in data:
            st = wx.StaticText(parent=parent, id=-1, label=label)
            tc = wx.TextCtrl(parent=parent, id=-1, value='', size=(100, -1))
            stcSizer.Add(item=st, proportion=0, flag=wx.ALIGN_CENTER_VERTICAL)
            stcSizer.Add(item=tc, proportion=0)
        return stcSizer

    #---------------------------------------------------------------------------- Handler

    def OnCloseWindow(self, event):
        self.Destroy()

    def OnOpen(self, event): pass
    def OnCopy(self, event): pass
    def OnCut(self, event): pass
    def OnPaste(self, event): pass
    def OnOption(self, event): pass
    def OnFirst(self, event): pass
    def OnPrev(self, event): pass
    def OnNext(self, event): pass
    def OnLast(self, event): pass

class App(wx.App):

    def OnInit(self):
        self.frame = Frame()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()



