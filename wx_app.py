import wx
def load(event):
	file = open(filename.GetValue())
	contents.SetValue(file.read())
	file.close()

def save(event):
	file = open(filename.GetValue(), 'w')
	file.write(contents.GetValue())
	file.close()

app = wx.App()
win = wx.Frame(None, title = "Simple Editor", size = (410, 335))

bkg = wx.Panel(win)

loadButton = wx.Button(bkg, label = 'Open',
					pos = (255, 5), size = (80, 25))

loadButton.Bind(wx.EVT_BUTTON, load)

saveButton = wx.Button(bkg, label = 'Close',)
saveButton.Bind(wx.Button, save)

filename = wx.TextCtrl(bkg)

contents = wx.TextCtrl(bkg, style = wx.TE_MULTILINE | wx.HSCROLL)

hbox = wx.BoxSizer()
hbox.Add(filename, proportion = 1, flag = wx.EXPEND)
hbox.Add(loadButton, proportion = 0, flag = wx.LEFT, border = 5)
hbox.Add(saveButton, proportion = 0, flag = ex.LEFT, border = 5)

vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox, proportion = 0, flag = wx.EXPEND | wx.ALL, border = 5)
vbox.Add(contents, proportion = 1, 
		flag = wx.EXPEND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border = 5)

bkg.SetSizer(vbox)
win.Show()