#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Use validator to check all text ctrl have data.
#          Note, in Dialog, the validator will invoked automatically when you press the Dialog's Ok button (to close the Dialog).
#-----------------------------------------------------------------------------

import wx

about_txt = """\
The validator used in this example will ensure that the text controls are 
not empty when you press the Ok button, and will not let you leave if 
any of the Validations fail.\
"""

# create the validator subclass
class NotEmptyValidator(wx.PyValidator):

    def __init__(self):
        super(self.__class__, self).__init__()

    def Clone(self):
        """
        NOTE that every validator must implement the Clone() method.
        """
        return NotEmptyValidator()

    def Validate(self, win):  # override the base class method: Validate(self, Window parent) -> bool
        textCtrl = self.GetWindow()  # get current validated window's reference
        text = textCtrl.GetValue().strip()

        if len(text) == 0:
            wx.MessageBox(message='This field must contain some text!', caption='Error')
            textCtrl.SetBackgroundColour('pink')
            textCtrl.SetFocus()  # Set's the focus to this window, allowing it to receive keyboard input
            textCtrl.Refresh()
            return False
        else:
            textCtrl.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
            textCtrl.Refresh()
            return True

    def TransferToWindow(self):
        return True

    def TransferFromWindow(self):
        return True

#-----------------------------------------------------------------------------

class Dialog(wx.Dialog):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='Validator')

        # create text controls
        about = wx.StaticText(parent=self, id=-1, label=about_txt)
        name_lable = wx.StaticText(parent=self, id=-1, label='Name:')
        email_label = wx.StaticText(parent=self, id=-1, label='Email:')
        phone_label = wx.StaticText(parent=self, id=-1, label='Phone:')

        name_text = wx.TextCtrl(parent=self, validator=NotEmptyValidator())
        email_text = wx.TextCtrl(parent=self, validator=NotEmptyValidator())
        phone_text = wx.TextCtrl(parent=self, validator=NotEmptyValidator())

        # create button
        ok = wx.Button(parent=self, id=wx.ID_OK)
        ok.SetDefault()
        cancel = wx.Button(parent=self, id=wx.ID_CANCEL)

        # layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(item=about, proportion=0, flag=wx.ALL, border=5)
        sizer.Add(item=wx.StaticLine(self), proportion=0, flag=wx.EXPAND | wx.ALL, border=5)

        fgsizer = wx.FlexGridSizer(rows=3, cols=2, vgap=5, hgap=5)
        fgsizer.Add(item=name_lable, proportion=0, flag=wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        fgsizer.Add(item=name_text, proportion=0, flag=wx.EXPAND)
        fgsizer.Add(item=email_label, proportion=0, flag=wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        fgsizer.Add(item=email_text, proportion=0, flag=wx.EXPAND)
        fgsizer.Add(item=phone_label, proportion=0, flag=wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        fgsizer.Add(item=phone_text, proportion=0, flag=wx.EXPAND)
        fgsizer.AddGrowableCol(1)
        sizer.Add(item=fgsizer, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)

        # NOTE, for dialog button, have sizer to make it in right place
        btns = wx.StdDialogButtonSizer()
        btns.AddButton(button=ok)
        btns.AddButton(button=cancel)
        btns.Realize()
        sizer.Add(item=btns, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)

        self.SetSizer(sizer)
        # sizer.Fit(self)
        sizer.SetSizeHints(self)
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




