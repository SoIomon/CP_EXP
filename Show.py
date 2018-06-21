# coding=utf-8
import wx
from math import *
from calcyacc import GetData,GetResult


class Calculator(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "计算器", size=(350, 480),
                          style=wx.DEFAULT_FRAME_STYLE ^ (wx.RESIZE_BORDER |
                                                          wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX))
        panel = wx.Panel(self)
        boxsize = wx.BoxSizer(wx.VERTICAL)
        gridBox = wx.GridSizer(rows=5, cols=5, hgap=5, vgap=5)
        self.equation = ""  # 记录等式

        self.textprint = wx.TextCtrl(panel, -1, '', style=wx.TE_MULTILINE | wx.TE_READONLY)

        # 按钮数据
        self.buttonData = "7 8 9 DEL AC 4 5 6 * / 1 2 3 + - 0  ( ) . = sin cos".split()
        buttonLength = len(self.buttonData)
        for i in range(buttonLength):
            labels = "%s" % self.buttonData[i]
            buttonIterm = wx.Button(panel, i, labels, size=(63, 52))
            self.createHandler(buttonIterm, labels)
            gridBox.Add(buttonIterm, 0, 0)
        boxsize.Add(self.textprint, 1, wx.EXPAND)
        boxsize.Add(gridBox, 5, wx.EXPAND)
        panel.SetSizerAndFit(boxsize)

        # 创建处理方法

    def createHandler(self, button, labels):
        item = "DEL AC ="
        if labels not in item:
            self.Bind(wx.EVT_BUTTON, self.OnAppend, button)
        elif labels == 'DEL':
            self.Bind(wx.EVT_BUTTON, self.OnDel, button)
        elif labels == 'AC':
            self.Bind(wx.EVT_BUTTON, self.OnAc, button)
        elif labels == '=':
            self.Bind(wx.EVT_BUTTON, self.OnTarget, button)
            # 添加运算符与数字

    def OnAppend(self, event):
        eventbutton = event.GetEventObject()
        label = eventbutton.GetLabel()
        self.equation += label
        self.textprint.SetValue(self.equation)

    def OnDel(self, event):
        self.equation = self.equation[:-1]
        self.textprint.SetValue(self.equation)

    def OnAc(self, event):
        self.textprint.Clear()
        self.equation = ""


    def OnTarget(self, event):
        string = self.equation
        if '^' in string:
            string = string.replace('^', '**')
        try:
            GetData(string)
            target = GetResult()
            self.equation += '=' + str(target)
            self.textprint.SetValue(self.equation)
        except SyntaxError:
            dlg = wx.MessageDialog(self, '请输入正确的等式!', '请注意',
                                   wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()


if __name__ == '__main__':
    app = wx.App()
    frame = Calculator()
    frame.Show()
    app.MainLoop()