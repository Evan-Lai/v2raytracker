
import base64
import http
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
        self.master.geometry('729x465')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.style.configure('import_links.TButton',font=('宋体',9))
        self.import_links = Button(self.top, text='导入节点链接', command=self.import_links_Cmd, style='import_links.TButton')
        self.import_links.place(relx=0.022, rely=0.034, relwidth=0.133, relheight=0.06)

        self.List1Var = StringVar(value='List1')
        self.List1Font = Font(font=('宋体',9))
        self.List1 = Listbox(self.top, listvariable=self.List1Var,font=self.List1Font)
        self.List1.place(relx=0.022, rely=0.172, relwidth=0.967, relheight=0.783)

        self.style.configure('track_links.TButton',font=('宋体',9))
        self.track_links = Button(self.top, text='跟踪选中链接', command=self.track_links_Cmd, style='track_links.TButton')
        self.track_links.place(relx=0.165, rely=0.034, relwidth=0.155, relheight=0.06)

        self.style.configure('clear_links.TButton',font=('宋体',9))
        self.clear_links = Button(self.top, text='清除不可用链接', command=self.clear_links_Cmd, style='clear_links.TButton')
        self.clear_links.place(relx=0.329, rely=0.034, relwidth=0.155, relheight=0.06)

        self.style.configure('to_sublink.TButton',font=('宋体',9))
        self.to_sublink = Button(self.top, text='生成订阅地址', command=self.to_sublink_Cmd, style='to_sublink.TButton')
        self.to_sublink.place(relx=0.494, rely=0.034, relwidth=0.133, relheight=0.06)

        self.style.configure('ping_links.TButton',font=('宋体',9))
        self.ping_links = Button(self.top, text='Ping测试选中链接', command=self.ping_links_Cmd, style='ping_links.TButton')
        self.ping_links.place(relx=0.647, rely=0.034, relwidth=0.144, relheight=0.054)

        self.VScroll1 = Scrollbar(self.top, orient='vertical')
        self.VScroll1.place(relx=0.966, rely=0.172, relwidth=0.023, relheight=0.776)

        self.style.configure('link_name.TLabel',anchor='w', font=('宋体',9))
        self.link_name = Label(self.top, text='节点别名', style='link_name.TLabel')
        self.link_name.place(relx=0.022, rely=0.138, relwidth=0.089, relheight=0.037)

        self.style.configure('address.TLabel',anchor='w', font=('宋体',9))
        self.address = Label(self.top, text='地址', style='address.TLabel')
        self.address.place(relx=0.132, rely=0.138, relwidth=0.254, relheight=0.037)

        self.style.configure('link_port.TLabel',anchor='w', font=('宋体',9))
        self.link_port = Label(self.top, text='端口', style='link_port.TLabel')
        self.link_port.place(relx=0.417, rely=0.138, relwidth=0.166, relheight=0.037)

        self.style.configure('link_style.TLabel',anchor='w', font=('宋体',9))
        self.link_style = Label(self.top, text='加密方式', style='link_style.TLabel')
        self.link_style.place(relx=0.615, rely=0.138, relwidth=0.078, relheight=0.037)

        self.style.configure('link_license.TLabel',anchor='w', font=('宋体',9))
        self.link_license = Label(self.top, text='协议', style='link_license.TLabel')
        self.link_license.place(relx=0.735, rely=0.138, relwidth=0.056, relheight=0.037)

        self.style.configure('link_speed.TLabel',anchor='w', font=('宋体',9))
        self.link_speed = Label(self.top, text='测速结果', style='link_speed.TLabel')
        self.link_speed.place(relx=0.834, rely=0.138, relwidth=0.089, relheight=0.037)


class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def import_links_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def track_links_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def clear_links_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def to_sublink_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def ping_links_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()
    
