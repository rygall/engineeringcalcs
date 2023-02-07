from tkinter import *
from tkinter import ttk


class root:

    def __init__(self):
        self.root = Tk()
        self.root.title("Engineering Calculations")
        icon = PhotoImage(file="icon.png")
        self.root.iconphoto(True, icon)
        bf = buttonframe(self.root)
        cf = calculationframe(self.root)
        self.root.mainloop()


class buttonframe:

    def __init__(self, rt):

        # initializing widgets
        self.frame = ttk.Frame(rt)

        self.headerbar = ttk.Frame(self.frame, relief='flat', borderwidth=0)
        self.addbutton = ttk.Button(self.headerbar, text="Add", command=self.add(), takefocus=0)
        self.deletebutton = ttk.Button(self.headerbar, text="Delete", command=self.delete(), takefocus=0)
        self.movebutton = ttk.Button(self.headerbar, text="Move", command=self.move(), takefocus=0)

        self.separator = ttk.Separator(self.frame, orient=HORIZONTAL)

        self.buttonland = ttk.Frame(self.frame, padding=20)
        self.testbutton = ttk.Button(self.buttonland, text="test")

        # building the geometry
        self.frame.grid(column=0, row=0, sticky='nw')

        self.headerbar.grid(column=0, row=0, sticky='nw')

        self.addbutton.grid(column=0, row=0)
        self.deletebutton.grid(column=1, row=0)
        self.movebutton.grid(column=2, row=0)

        self.separator.grid(column=0, row=1, sticky='nw')

        self.buttonland.grid(column=0, row=2)
        self.testbutton.grid(column=0, row=0)

    def add(self):
        pass

    def delete(self):
        pass

    def move(self):
        pass


class calculationframe:

    def __init__(self, rt):

        # initializing widgets
        self.frame = ttk.Frame(rt)

        self.headerbar = ttk.Frame(self.frame, relief='flat', borderwidth=0)
        self.clearbutton = ttk.Button(self.headerbar, text="Clear", command=self.clear(), takefocus=0)
        self.resetbutton = ttk.Button(self.headerbar, text="Reset", command=self.reset(), takefocus=0)
        self.calculatebutton = ttk.Button(self.headerbar, text="Calculate", command=self.calculate(), takefocus=0)
        self.exportbutton = ttk.Button(self.headerbar, text="Export", command=self.export(), takefocus=0)

        self.separator = ttk.Separator(self.frame, orient=HORIZONTAL)

        self.calculateland = ttk.Frame(self.frame, padding=15)

        # building the geometry
        self.frame.grid(column=5, row=0, sticky='nw')

        self.headerbar.grid(column=0, row=0, sticky='nw')

        self.clearbutton.grid(column=0, row=0)
        self.resetbutton.grid(column=1, row=0)
        self.calculatebutton.grid(column=2, row=0)
        self.exportbutton.grid(column=3, row=0)

        self.separator.grid(column=0, row=1, sticky='nw')

        self.calculateland.grid(column=0, row=2, sticky='nw')


    def clear(self):
        pass

    def reset(self):
        pass

    def calculate(self):
        pass

    def export(self):
        pass


root()

