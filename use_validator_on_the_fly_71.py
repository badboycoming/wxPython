#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: validator data on the fly.
#          Note, on the fly only can used with Dialog, cannot used with Frame ...? now cannot find method with frame :(
#-----------------------------------------------------------------------------

import wx
import string

about_txt = """\
The validator used in this example validate the input on the fly instead of waiting
until the ok button is pressed. The first field not allow digits to be typed, the
second allow anything and the third not allow alphabetic characters to be entered.\
"""

class CharValidator(wx.PyValidator):

    def __init__(self, flag):
        super(self.__class__, self).__init__()
        self.flag = flag
        self.Bind(event=wx.EVT_CHAR, handler=self.OnChar)

    def Clone(self):
        """
        Note that every validator must implement the Clone() method.
        """
        return CharValidator(self.flag)

    def Validate(self, win):
        return True  # here just stub

    def TransferToWindow(self):
        return True  # here just stub

    def TransferFromWindow(self):
        return True  # here just stub

    def OnChar(self, event):
        key = chr(event.GetKeyCode())
        if self.flag == 'no-alpha' and key in string.letters:
            return
        if self.flag == 'no-digit' and key in string.digits:
            return

        # NOTE, if the above two invalid condition happened, then returned, not execute
        # following skip, so the input will be blocked.
        event.Skip()

class Dialog(wx.Dialog):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='Validator')

        about = wx.StaticText(parent=self, id=-1, label=about_txt)
        name_label = wx.StaticText(parent=self, id=-1, label='Name:')
        email_label = wx.StaticText(parent=self, id=-1, label='Email:')
        phone_label = wx.StaticText(parent=self, id=-1, label='Phone:')

        # binding the validator
        name_txt = wx.TextCtrl(parent=self, validator=CharValidator('no-digit'))
        email_txt = wx.TextCtrl(parent=self, validator=CharValidator('any'))
        phone_txt = wx.TextCtrl(parent=self, validator=CharValidator('no-alpha'))

        ok = wx.Button(parent=self, id=wx.ID_OK)
        ok.SetDefault()
        cancel = wx.Button(parent=self, id=wx.ID_CANCEL)

        # layout
        sizer = wx.BoxSizer(wx.VERTICAL)

        sizer.Add(item=about, proportion=0, flag=wx.ALL, border=5)
        sizer.Add(item=wx.StaticLine(self), proportion=0, flag=wx.EXPAND|wx.ALL, border=5)

        fgsizer = wx.FlexGridSizer(rows=3, cols=2, hgap=5, vgap=5)
        fgsizer.Add(item=name_label, proportion=0, flag=wx.ALIGN_RIGHT)
        fgsizer.Add(item=name_txt, proportion=0, flag=wx.EXPAND)
        fgsizer.Add(item=email_label, proportion=0, flag=wx.ALIGN_RIGHT)
        fgsizer.Add(item=email_txt, proportion=0, flag=wx.EXPAND)
        fgsizer.Add(item=phone_label, proportion=0, flag=wx.ALIGN_RIGHT)
        fgsizer.Add(item=phone_txt, proportion=0, flag=wx.EXPAND)
        fgsizer.AddGrowableCol(1)
        sizer.Add(item=fgsizer, proportion=0, flag=wx.EXPAND|wx.ALL, border=5)

        btns = wx.StdDialogButtonSizer()
        btns.AddButton(ok)
        btns.AddButton(cancel)
        btns.Realize()
        sizer.Add(item=btns, proportion=0, flag=wx.EXPAND|wx.ALL, border=5)

        self.SetSizer(sizer)
        sizer.Fit(self)

        self.CenterOnScreen()

class App(wx.App):

    def OnInit(self):
        dlg = Dialog()
        dlg.ShowModal()
        dlg.Destroy()
        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()




