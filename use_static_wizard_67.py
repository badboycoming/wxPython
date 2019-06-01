#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Use static wizard dialog.
#-----------------------------------------------------------------------------

import wx
import wx.wizard

class TitlePage(wx.wizard.WizardPageSimple):

    def __init__(self, parent, title):
        super(self.__class__, self).__init__(parent=parent)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.sizer)

        titleText = wx.StaticText(parent=self, id=-1, label=title)
        titleText.SetFont(font=wx.Font(pointSize=18, family=wx.MODERN, style=wx.NORMAL, weight=wx.BOLD))

        self.sizer.Add(item=titleText, proportion=0, flag=wx.ALIGN_CENTER | wx.ALL, border=5)
        self.sizer.Add(item=wx.StaticLine(parent=self, id=-1), proportion=0, flag=wx.EXPAND | wx.ALL, border=5)

#-----------------------------------------------------------------------------

class App(wx.App):

    def OnInit(self):

        wz = wx.wizard.Wizard(parent=None, id=-1, title='Wizard demo')

        # create wizard pages
        page1 = TitlePage(parent=wz, title='Page 1')
        page2 = TitlePage(parent=wz, title='Page 2')
        page3 = TitlePage(parent=wz, title='Page 3')
        page4 = TitlePage(parent=wz, title='Page 4')

        ### NOTE: here add widgets outside of the definition class
        page1.sizer.Add(item=wx.StaticText(parent=page1, id=-1, label='This is the first page'), proportion=0, flag=wx.ALIGN_CENTER)
        page4.sizer.Add(item=wx.StaticText(parent=page4, id=-1, label='This is the last page'), proportion=0, flag=wx.ALIGN_CENTER)

        # create page chain
        wx.wizard.WizardPageSimple_Chain(first=page1, second=page2)
        wx.wizard.WizardPageSimple_Chain(first=page2, second=page3)
        wx.wizard.WizardPageSimple_Chain(first=page3, second=page4)

        # sizing
        # wz.FitToPage(page1)

        if wz.RunWizard(firstPage=page1):
            print 'Succeed'

        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()



