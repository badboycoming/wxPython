#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Use validator to check all text ctrl have data.
#          Note, in Frame, the validator not invoked automatically, you should invoke the Validate by yourself.
#-----------------------------------------------------------------------------

import wx

about_txt = """\
The validator used in this example will ensure that the text controls are \
not empty when you press the Ok button, and will not let you leave if \
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
            wx.MessageBox(message='Invalid Empty Field !', caption='Error')
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

#----------------------------------------------------------------------------- not use panel

# # class Dialog(wx.Dialog):
# class Frame(wx.Frame):
#
#     def __init__(self):
#         super(self.__class__, self).__init__(parent=None, id=-1, title='Validator', style=wx.DEFAULT_FRAME_STYLE|wx.WS_EX_VALIDATE_RECURSIVELY)
#         self.SetBackgroundColour('White')
#
#         # create text controls
#         about = wx.StaticText(parent=self, id=-1, label=about_txt)
#         about.Wrap(500)
#         name_lable = wx.StaticText(parent=self, id=-1, label='Name:')
#         email_label = wx.StaticText(parent=self, id=-1, label='Email:')
#         phone_label = wx.StaticText(parent=self, id=-1, label='Phone:')
#
#         name_text = wx.TextCtrl(parent=self, validator=NotEmptyValidator())
#         email_text = wx.TextCtrl(parent=self, validator=NotEmptyValidator())
#         phone_text = wx.TextCtrl(parent=self, validator=NotEmptyValidator())
#
#         # create button
#         ok = wx.Button(parent=self, id=wx.ID_OK)
#         ok.SetDefault()
#         cancel = wx.Button(parent=self, id=wx.ID_CANCEL)
#         self.Bind(event=wx.EVT_BUTTON, handler=self.OnOk, source=ok)
#         self.Bind(event=wx.EVT_BUTTON, handler=self.OnCancel, source=cancel)
#
#         # layout
#         sizer = wx.BoxSizer(wx.VERTICAL)
#         sizer.Add(item=about, proportion=0, flag=wx.ALL, border=5)
#         sizer.Add(item=wx.StaticLine(self), proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
#
#         fgsizer = wx.FlexGridSizer(rows=3, cols=2, vgap=5, hgap=5)
#         fgsizer.Add(item=name_lable, proportion=0, flag=wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
#         fgsizer.Add(item=name_text, proportion=0, flag=wx.EXPAND)
#         fgsizer.Add(item=email_label, proportion=0, flag=wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
#         fgsizer.Add(item=email_text, proportion=0, flag=wx.EXPAND)
#         fgsizer.Add(item=phone_label, proportion=0, flag=wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
#         fgsizer.Add(item=phone_text, proportion=0, flag=wx.EXPAND)
#         fgsizer.AddGrowableCol(1)
#         sizer.Add(item=fgsizer, proportion=0, flag=wx.EXPAND|wx.ALL, border=5)
#
#         # NOTE, for dialog button, have sizer to make it in right place
#         btns = wx.StdDialogButtonSizer()
#         btns.AddButton(button=ok)
#         btns.AddButton(button=cancel)
#         btns.Realize()
#         sizer.Add(item=btns, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
#
#         self.SetSizer(sizer)
#         # sizer.Fit(self)
#         sizer.SetSizeHints(self)
#         self.CenterOnScreen()
#
#     def OnOk(self, event):
#         rtv = self.Validate()
#         if rtv:
#             print 'All validator are Ok :)'
#         else:
#             print 'Invalid validator found :('
#
#     def OnCancel(self, event):
#         self.Destroy()

#----------------------------------------------------------------------------- use panel

# class Dialog(wx.Dialog):
class Frame(wx.Frame):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='Validator') #, style=wx.DEFAULT_FRAME_STYLE|wx.WS_EX_VALIDATE_RECURSIVELY)
        self.panel = wx.Panel(parent=self, id=-1) #, style=wx.WS_EX_VALIDATE_RECURSIVELY)   ###---> style flag seems no use, only validate one sub widget at one time
        self.panel.SetBackgroundColour('White')

        # create text controls
        about = wx.StaticText(parent=self.panel, id=-1, label=about_txt)
        about.Wrap(500)
        name_lable = wx.StaticText(parent=self.panel, id=-1, label='Name:')
        email_label = wx.StaticText(parent=self.panel, id=-1, label='Email:')
        phone_label = wx.StaticText(parent=self.panel, id=-1, label='Phone:')

        name_text = wx.TextCtrl(parent=self.panel, validator=NotEmptyValidator())
        email_text = wx.TextCtrl(parent=self.panel, validator=NotEmptyValidator())
        phone_text = wx.TextCtrl(parent=self.panel, validator=NotEmptyValidator())

        # create button
        ok = wx.Button(parent=self.panel, id=wx.ID_OK)
        ok.SetDefault()
        cancel = wx.Button(parent=self.panel, id=wx.ID_CANCEL)
        self.Bind(event=wx.EVT_BUTTON, handler=self.OnOk, source=ok)
        self.Bind(event=wx.EVT_BUTTON, handler=self.OnCancel, source=cancel)

        # layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(item=about, proportion=0, flag=wx.ALL, border=5)
        sizer.Add(item=wx.StaticLine(self.panel), proportion=0, flag=wx.EXPAND | wx.ALL, border=5)

        fgsizer = wx.FlexGridSizer(rows=3, cols=2, vgap=5, hgap=5)
        fgsizer.Add(item=name_lable, proportion=0, flag=wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        fgsizer.Add(item=name_text, proportion=0, flag=wx.EXPAND)
        fgsizer.Add(item=email_label, proportion=0, flag=wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        fgsizer.Add(item=email_text, proportion=0, flag=wx.EXPAND)
        fgsizer.Add(item=phone_label, proportion=0, flag=wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        fgsizer.Add(item=phone_text, proportion=0, flag=wx.EXPAND)
        fgsizer.AddGrowableCol(1)
        sizer.Add(item=fgsizer, proportion=0, flag=wx.EXPAND|wx.ALL, border=5)

        # NOTE, for dialog button, have sizer to make it in right place
        btns = wx.StdDialogButtonSizer()
        btns.AddButton(button=ok)
        btns.AddButton(button=cancel)
        btns.Realize()
        sizer.Add(item=btns, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)

        self.panel.SetSizer(sizer)
        # sizer.Fit(self)
        sizer.SetSizeHints(self)
        self.CenterOnScreen()

    def OnOk(self, event):
        rtv = self.panel.Validate()
        if rtv:
            print 'All validator are Ok :)'
        else:
            print 'Invalid validator found :('

    def OnCancel(self, event):
        self.Destroy()

class App(wx.App):

    def OnInit(self):
        # dlg = Dialog()
        # dlg.ShowModal()
        # dlg.Destroy()
        frame = Frame()
        self.SetTopWindow(frame)
        frame.Show()
        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()



