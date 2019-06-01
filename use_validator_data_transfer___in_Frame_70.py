#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: validator data transfer.
#          Note, in Frame, the TransferToWindow should invoked manully when you open the Frame.
#          Note, in Frame, the TransferFromWindow should invoked manully when you press the Ok button (to close the Frame).
#-----------------------------------------------------------------------------

import wx
import pprint

about_txt = """\
The validator used in this example shows how the validator can be used to 
transfer data to and from each text control automatically when the dialog 
is shown and dismissed.\
"""

class DataXferValidator(wx.PyValidator):

    def __init__(self, data, key):
        super(self.__class__, self).__init__()
        self.data = data
        self.key = key

    def Clone(self):
        """
        Note that every validator must implement the Clone() method.
        """
        return DataXferValidator(self.data, self.key)

    def Validate(self, win):
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

    def TransferToWindow(self):  # called on dialog open
        textCtrl = self.GetWindow()
        # textCtrl.SetValue(self.data.get(self.key, ''))
        textCtrl.SetValue(self.data.setdefault(self.key, ''))
        return True

    def TransferFromWindow(self):  # called on dialog close
        textCtrl = self.GetWindow()
        self.data[self.key] = textCtrl.GetValue()
        return True

#----------------------------------------------------------------------------- not use panel

# # class Dialog(wx.Dialog):
# class Frame(wx.Frame):
#
#     def __init__(self, data):
#         super(self.__class__, self).__init__(parent=None, id=-1, title='Validator')
#         self.SetBackgroundColour('White')
#         self.data = data
#
#         about = wx.StaticText(parent=self, id=-1, label=about_txt)
#         name_lable = wx.StaticText(parent=self, id=-1, label='Name:')
#         email_label = wx.StaticText(parent=self, id=-1, label='Email:')
#         phone_label = wx.StaticText(parent=self, id=-1, label='Phone:')
#
#         name_text = wx.TextCtrl(parent=self, validator=DataXferValidator(self.data, 'name'))
#         email_text = wx.TextCtrl(parent=self, validator=DataXferValidator(self.data, 'email'))
#         phone_text = wx.TextCtrl(parent=self, validator=DataXferValidator(self.data, 'phone'))
#
#         ok = wx.Button(parent=self, id=wx.ID_OK)
#         ok.SetDefault()
#         cancel= wx.Button(parent=self, id=wx.ID_CANCEL)
#         self.Bind(event=wx.EVT_BUTTON, handler=self.OnOk, source=ok)
#         self.Bind(event=wx.EVT_BUTTON, handler=self.OnCancel, source=cancel)
#
#         # layout
#         sizer = wx.BoxSizer(wx.VERTICAL)
#         sizer.Add(item=about, proportion=0, flag=wx.ALL, border=5)
#         sizer.Add(item=wx.StaticLine(self), proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
#
#         fgsizer = wx.FlexGridSizer(rows=3, cols=2, hgap=5, vgap=5)
#         fgsizer.Add(item=name_lable, proportion=0, flag=wx.ALIGN_RIGHT)
#         fgsizer.Add(item=name_text, proportion=0, flag=wx.EXPAND)
#         fgsizer.Add(item=email_label, proportion=0, flag=wx.ALIGN_RIGHT)
#         fgsizer.Add(item=email_text, proportion=0, flag=wx.EXPAND)
#         fgsizer.Add(item=phone_label, proportion=0, flag=wx.ALIGN_RIGHT)
#         fgsizer.Add(item=phone_text, proportion=0, flag=wx.EXPAND)
#         fgsizer.AddGrowableCol(1)
#         sizer.Add(item=fgsizer, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
#
#         btns = wx.StdDialogButtonSizer()
#         btns.AddButton(ok)
#         btns.AddButton(cancel)
#         btns.Realize()
#         sizer.Add(item=btns, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
#
#         self.TransferDataToWindow()  ###---> when create Frame, invoke manully to fill data to Frame widgets
#
#         self.SetSizer(sizer)
#         sizer.SetSizeHints(self)
#         self.CenterOnScreen()
#
#     def OnOk(self, event):
#         self.Validate()   ###---> also invokde manully for validate the Frame widgets contents
#
#     def OnCancel(self, event):
#         self.TransferDataFromWindow()   ###---> when close Frame, invoke manully to get data from Frame widgets
#         self.Destroy()
#
#         # only for test
#         wx.MessageBox(message="You entered these values:\n\n" + pprint.pformat(self.data), caption='Info')

#----------------------------------------------------------------------------- use panel

# class Dialog(wx.Dialog):
class Frame(wx.Frame):

    def __init__(self, data):
        super(self.__class__, self).__init__(parent=None, id=-1, title='Validator')
        self.data = data
        self.panel = wx.Panel(parent=self, id=-1, style=wx.WS_EX_VALIDATE_RECURSIVELY)
        self.panel.SetBackgroundColour('White')

        about = wx.StaticText(parent=self.panel, id=-1, label=about_txt)
        name_lable = wx.StaticText(parent=self.panel, id=-1, label='Name:')
        email_label = wx.StaticText(parent=self.panel, id=-1, label='Email:')
        phone_label = wx.StaticText(parent=self.panel, id=-1, label='Phone:')

        name_text = wx.TextCtrl(parent=self.panel, validator=DataXferValidator(self.data, 'name'))
        email_text = wx.TextCtrl(parent=self.panel, validator=DataXferValidator(self.data, 'email'))
        phone_text = wx.TextCtrl(parent=self.panel, validator=DataXferValidator(self.data, 'phone'))

        ok = wx.Button(parent=self.panel, id=wx.ID_OK)
        ok.SetDefault()
        cancel= wx.Button(parent=self.panel, id=wx.ID_CANCEL)
        self.Bind(event=wx.EVT_BUTTON, handler=self.OnOk, source=ok)
        self.Bind(event=wx.EVT_BUTTON, handler=self.OnCancel, source=cancel)

        # layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(item=about, proportion=0, flag=wx.ALL, border=5)
        sizer.Add(item=wx.StaticLine(self.panel), proportion=0, flag=wx.EXPAND | wx.ALL, border=5)

        fgsizer = wx.FlexGridSizer(rows=3, cols=2, hgap=5, vgap=5)
        fgsizer.Add(item=name_lable, proportion=0, flag=wx.ALIGN_RIGHT)
        fgsizer.Add(item=name_text, proportion=0, flag=wx.EXPAND)
        fgsizer.Add(item=email_label, proportion=0, flag=wx.ALIGN_RIGHT)
        fgsizer.Add(item=email_text, proportion=0, flag=wx.EXPAND)
        fgsizer.Add(item=phone_label, proportion=0, flag=wx.ALIGN_RIGHT)
        fgsizer.Add(item=phone_text, proportion=0, flag=wx.EXPAND)
        fgsizer.AddGrowableCol(1)
        sizer.Add(item=fgsizer, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)

        btns = wx.StdDialogButtonSizer()
        btns.AddButton(ok)
        btns.AddButton(cancel)
        btns.Realize()
        sizer.Add(item=btns, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)

        self.panel.TransferDataToWindow()  ###---> when create Frame, invoke manully to fill data to Frame widgets

        self.panel.SetSizer(sizer)
        sizer.SetSizeHints(self)
        self.CenterOnScreen()

    def OnOk(self, event):
        self.panel.Validate()   ###---> also invokde manully for validate the Frame widgets contents

    def OnCancel(self, event):
        self.panel.TransferDataFromWindow()   ###---> when close Frame, invoke manully to get data from Frame widgets
        self.Destroy()

        # only for test
        wx.MessageBox(message="You entered these values:\n\n" + pprint.pformat(self.data), caption='Info')


class App(wx.App):

    def OnInit(self):
        # data = {'name': 'Peter Pan'}
        # dlg = Dialog(data)
        # dlg.ShowModal()
        # dlg.Destroy()

        data = {'name': 'Peter Pan'}
        frame = Frame(data)
        self.SetTopWindow(frame)
        frame.Show()

        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()



