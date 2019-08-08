from tkinter import Frame, Tk, BOTH, Text, Menu, END
#import tkFileDialog 
from tkinter import *
from tkdocviewer import *
import tkinter.filedialog

root = Tk()
class Example(Frame):

    def init(self, parent):
        Frame.init(self, parent)

        self.parent = parent
        self.initUI()

    def initUI(self):

        self.parent.title("File dialog")
        # self.pack(fill=BOTH, expand=1)


        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Open", command=self.onOpen)
        menubar.add_cascade(label="File", menu=fileMenu)

        # self.txt = Text(self)
        # self.txt.pack(fill=BOTH, expand=1)


    def onOpen(self):

        ftypes = [('Python files', '.pdf'), ('All files', '')]
        #dlg = tkinter.filedialog.Open(self, filetypes = ftypes)
        dlg = tkinter.filedialog.Open(self, filetypes = ftypes)
        fl = dlg.show()


        if fl != '':
            text = self.readFile(fl)
            # self.txt.insert(END, text)

    def readFile(self, filename):
        # Create a DocViewer widget
        v = DocViewer(root)
        v.pack(side="top", expand=1, fill="both")
        v.display_file(filename)


def main():
    self = DocViewer(root)
    ex = Example(root)
    root.geometry("300x250+300+300")
    root.mainloop()


if name == 'main':
    main()
