#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: real world.
#-----------------------------------------------------------------------------

import wx

class Frame(wx.Frame):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='Real World')
        panel = wx.Panel(parent=self)

        # At first, create the controls
        topLabel = wx.StaticText(parent=panel, id=-1, label='Account Information')
        topLabel.SetFont(font=wx.Font(pointSize=18, family=wx.SWISS, style=wx.NORMAL, weight=wx.BOLD))

        nameLabel = wx.StaticText(parent=panel, id=-1, label='Name:')
        name = wx.TextCtrl(parent=panel, id=-1, value='')

        addrLabel = wx.StaticText(parent=panel, id=-1, label='Address:')
        addr1 = wx.TextCtrl(parent=panel, id=-1, value='')
        addr2 = wx.TextCtrl(parent=panel, id=-1, value='')

        cszLabel = wx.StaticText(parent=panel, id=-1, label='City, State, Zip:')
        city = wx.TextCtrl(parent=panel, id=-1, value='', size=(150, -1))
        state = wx.TextCtrl(parent=panel, id=-1, value='', size=(50, -1))
        zip = wx.TextCtrl(parent=panel, id=-1, value='', size=(70, -1))

        phoneLabel = wx.StaticText(parent=panel, id=-1, label='Phone')
        phone = wx.TextCtrl(parent=panel, id=-1, value='')

        emailLabel = wx.StaticText(parent=panel, id=-1, label='Email:')
        email = wx.TextCtrl(parent=panel, id=-1, value='')

        saveBtn = wx.Button(parent=panel, id=-1, label='Save')
        cancelBtn = wx.Button(parent=panel, id=-1, label='Cancel')

        ##### Now do the layout

        # mainSizer is the top-level one that manages everything
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(item=topLabel, proportion=0, flag=wx.ALL, border=30)
        mainSizer.Add(item=wx.StaticLine(parent=panel), proportion=0, flag=wx.EXPAND|wx.TOP|wx.BOTTOM, border=5)

        # subsizer is a grid that holds all of the info
        subSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
        subSizer.AddGrowableCol(idx=1)

        subSizer.Add(item=nameLabel, proportion=0, flag=wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        subSizer.Add(item=name, proportion=0, flag=wx.EXPAND)

        subSizer.Add(item=addrLabel, proportion=0, flag=wx.ALIGN_RIGHT|wx.ALIGN_CENTRE_VERTICAL)
        subSizer.Add(item=addr1, proportion=0, flag=wx.EXPAND)
        subSizer.Add((1, 1))  # some empty space
        subSizer.Add(item=addr2, proportion=0, flag=wx.EXPAND)

        subSizer.Add(item=cszLabel, proportion=0, flag=wx.ALIGN_RIGHT|wx.ALIGN_CENTRE_VERTICAL)

        # the city, state, zip in the cszSizer
        cszSizer = wx.BoxSizer(wx.HORIZONTAL)
        cszSizer.Add(item=city, proportion=1)
        cszSizer.Add(item=state, proportion=0, flag=wx.LEFT|wx.RIGHT, border=5)
        cszSizer.Add(item=zip)
        # add cszSizer to subSizer
        subSizer.Add(item=cszSizer, proportion=0, flag=wx.EXPAND)

        subSizer.Add(item=phoneLabel, proportion=0, flag=wx.ALIGN_RIGHT|wx.ALIGN_CENTRE_VERTICAL)
        subSizer.Add(item=phone, proportion=0, flag=wx.EXPAND)

        subSizer.Add(item=emailLabel, proportion=0, flag=wx.ALIGN_RIGHT|wx.ALIGN_CENTRE_VERTICAL)
        subSizer.Add(item=email, proportion=0, flag=wx.EXPAND)

        #### add subSizer to mainSizer
        mainSizer.Add(item=subSizer, proportion=0, flag=wx.EXPAND|wx.ALL, border=10)

        # button in the btnSizer
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer.Add(item=(1, 1), proportion=1)
        btnSizer.Add(item=saveBtn)
        btnSizer.Add(item=(1, 1), proportion=1)
        btnSizer.Add(item=cancelBtn)
        btnSizer.Add(item=(1, 1), proportion=1)

        #### add btnSizer to mainSizer
        mainSizer.Add(item=btnSizer, proportion=0, flag=wx.EXPAND|wx.BOTTOM, border=10)

        panel.SetSizer(mainSizer)
        mainSizer.Fit(self)
        mainSizer.SetSizeHints(self)  # to prevent the frame from getting smaller than this Fit size

class App(wx.App):

    def OnInit(self):
        self.frame = Frame()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()







