#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Use the class AbstractModel.
#-----------------------------------------------------------------------------

import wx
import AbstractModel

class SimpleName(AbstractModel.AbstractModel):
    def __init__(self, first='', last=''):
        super(self.__class__, self).__init__()
        self.set(first, last)

    def set(self, first, last):
        self.first = first
        self.last = last
        self.update()

class Frame(wx.Frame):
    def __init__(self, parent=None, id=-1):
        super(self.__class__, self).__init__(parent=parent, id=id, title='Cell Phone Brand', size=(600, 200))
        panel = wx.Panel(parent=self)
        panel.SetBackgroundColour('White')
        self.Bind(event=wx.EVT_CLOSE, handler=self.OnCloseWindow)

        btnSizer = self.__createButtonGroup(parent=panel)
        self.textFields = {}
        stcSizer = self.__createTextFields(parent=panel)

        self.model = SimpleName()
        self.model.addListener(self.OnUpdate)

        # layout
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(item=btnSizer, proportion=0, flag=wx.ALL^wx.RIGHT, border=5)
        mainSizer.Add(item=stcSizer, proportion=0, flag=wx.TOP|wx.BOTTOM|wx.ALIGN_CENTER, border=20)
        panel.SetSizer(mainSizer)
        mainSizer.SetSizeHints(self)
        self.CenterOnScreen()

    #------------------------------------------------------------------------- Create Button

    def __buttonData(self):
        return (
            ('Apple', self.OnApple),
            ('Samsung', self.OnSamsung),
            ('Huawei', self.OnHuawei),
            ('Oppo', self.OnOppo),
        )

    def __buildOnButton(self, parent, label, handler):
        btn = wx.Button(parent=parent, id=-1, label=label)
        self.Bind(event=wx.EVT_BUTTON, handler=handler, source=btn)
        return btn

    def __createButtonGroup(self, parent):
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        for label, handler in self.__buttonData():
            button = self.__buildOnButton(parent=parent, label=label, handler=handler)
            btnSizer.Add(item=button, proportion=0, flag=wx.RIGHT, border=5)
        return btnSizer

    #------------------------------------------------------------------------- Create Textfields

    def __textFieldData(self):
        return (
            ('Brand'),
            ('Country'),
        )

    def __createTextFields(self, parent):
        stcSizer = wx.FlexGridSizer(rows=2, cols=2, hgap=5, vgap=5)
        for label in self.__textFieldData():
            stc = wx.StaticText(parent=parent, id=-1, label=label)
            txt = wx.TextCtrl(parent=parent, id=-1, value='', size=(100, -1), style=wx.TE_READONLY)
            self.textFields[label] = txt
            stcSizer.Add(item=stc, proportion=0, flag=wx.ALIGN_CENTER_VERTICAL)
            stcSizer.Add(item=txt, proportion=0)
        return stcSizer

    #------------------------------------------------------------------------- Update Textfields

    def OnUpdate(self, mdl):
        self.textFields['Brand'].SetValue(mdl.first)
        self.textFields['Country'].SetValue(mdl.last)

    def OnApple(self, event):
        self.model.set(first='Apple', last='U.S.')

    def OnSamsung(self, event):
        self.model.set(first='Samsung', last='Kroea')

    def OnHuawei(self, event):
        self.model.set(first='Huawei', last='China')

    def OnOppo(self, event):
        self.model.set(first='Oppo', last='China')

    def OnCloseWindow(self, event):
        self.Destroy()

class App(wx.App):
    def OnInit(self):
        self.frame = Frame()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':
    app = App()
    app.MainLoop()



