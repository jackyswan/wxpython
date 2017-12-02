import wx

app = wx.App()
win = wx.Frame(None, title = "", size = (410, 335))
win.Show()

loadButton = wx.Button(win, label = 'Open',
					pos = (255, 5), size = (80, 25))

saveButton = wx.Button(win, label = 'Close',
					pos = (315, 5), size = (80, 25))

filename = wx.TextCtrl(win, pos = (5, 5), size = (210, 25))

contents = wx.TextCtrl(win, pos = (5, 35))