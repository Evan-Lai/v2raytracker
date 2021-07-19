
import base64
import http
#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, sys
try:
    from tkinter import *
except ImportError:  #Python 2.x
    PythonVersion = 2
    from Tkinter import *
    from tkFont import Font
    from ttk import *
    #Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
    from tkMessageBox import *
    #Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
    #import tkFileDialog
    #import tkSimpleDialog
else:  #Python 3.x
    PythonVersion = 3
    from tkinter.font import Font
    from tkinter.ttk import *
    from tkinter.messagebox import *
    #import tkinter.filedialog as tkFileDialog
    #import tkinter.simpledialog as tkSimpleDialog    #askstring()

class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('V2rayTracker')
        self.master.geometry('820x465')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.style.configure('ping_links.TButton',font=('宋体',9))
        self.ping_links = Button(self.top, text='Ping测试选中链接', command=self.ping_links_Cmd, style='ping_links.TButton')
        self.ping_links.place(relx=0.647, rely=0.034, relwidth=0.144, relheight=0.054)

        self.style.configure('to_sublink.TButton',font=('宋体',9))
        self.to_sublink = Button(self.top, text='生成订阅地址', command=self.to_sublink_Cmd, style='to_sublink.TButton')
        self.to_sublink.place(relx=0.494, rely=0.034, relwidth=0.133, relheight=0.06)

        self.style.configure('clear_links.TButton',font=('宋体',9))
        self.clear_links = Button(self.top, text='清除不可用链接', command=self.clear_links_Cmd, style='clear_links.TButton')
        self.clear_links.place(relx=0.329, rely=0.034, relwidth=0.155, relheight=0.06)

        self.style.configure('track_links.TButton',font=('宋体',9))
        self.track_links = Button(self.top, text='跟踪选中链接', command=self.track_links_Cmd, style='track_links.TButton')
        self.track_links.place(relx=0.165, rely=0.034, relwidth=0.155, relheight=0.06)

        self.style.configure('import_links.TButton',font=('宋体',9))
        self.import_links = Button(self.top, text='导入节点链接', command=self.import_links_Cmd, style='import_links.TButton')
        self.import_links.place(relx=0.022, rely=0.034, relwidth=0.133, relheight=0.06)

        self.VScroll1 = Scrollbar(self.top, orient='vertical')
        self.VScroll1.place(relx=0.944, rely=0.155, relwidth=0.023, relheight=0.794)

        self.style.configure('TreeView1.Treeview',font=('宋体',9))
        self.InformationView = Treeview(self.top,show="headings",style='TreeView1.Treeview',yscrollcommand=self.VScroll1.set)
        self.InformationView['columns'] = ["节点别名","地址","端口","加密方式","测试结果","跟踪"]    #TODO在这里添加标题列表，第一列固定为树形显示
        self.InformationView.column("节点别名", width=100)
        self.InformationView.column("地址", width=100)
        self.InformationView.column("端口", width=100)
        self.InformationView.column("加密方式", width=100)
        self.InformationView.column("测试结果", width=100)
        self.InformationView.column("跟踪", width=100)
        self.InformationView.heading("节点别名", text="节点别名")
        self.InformationView.heading("地址", text="地址")
        self.InformationView.heading("端口", text="端口")
        self.InformationView.heading("加密方式", text="加密方式")
        self.InformationView.heading("测试结果", text="测试结果")
        self.InformationView.heading("跟踪", text="跟踪")
        self.VScroll1['command'] = self.InformationView.yview
        self.InformationView.insert('','end',values=['示例节点','127.0.0.1','8080','auto','100ms','可用'])
        self.InformationView.place(relx=0.022, rely=0.155, relwidth=0.945, relheight=0.794)


class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。

    function = function.Function()

    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def ping_links_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def to_sublink_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def clear_links_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def track_links_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def import_links_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()
    try: top.destroy()
    except: pass
