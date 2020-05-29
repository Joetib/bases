from tkinter import *
from tkinter import ttk
from bases.converter import Converter


class BaseGUI:
    value = None
    base_from = None
    base_to = None
    result = None

    __slots__ = 'value', 'base_from', 'base_to', 'result'

    def start_gui(self):
        root = Tk()
        root.title('Number Base Converter')
        
        mainframe = ttk.Frame(root, padding="100 60 60 100")
        
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)

        self.value = StringVar()
        self.base_from = StringVar()
        self.base_to = StringVar()
        self.result = StringVar()

        value_entry = ttk.Entry(mainframe, width=5, textvariable=self.value)
        value_entry.grid(column=1, row=2, sticky=(W, E))

        base_from_entry = ttk.Entry(mainframe, width=5, textvariable=self.base_from)
        base_from_entry.grid(column=2, row=2, sticky=(W, E))

        base_to_entry = ttk.Entry(mainframe, width=5, textvariable=self.base_to)
        base_to_entry.grid(column=3, row=2, sticky=(W, E))

        ttk.Label(mainframe, textvariable=self.result).grid(column=1, row=3, sticky=(W, E))
        ttk.Button(mainframe, text='convert', command=self.calculate).grid(column=2, row=3, sticky=(W, E))
        ttk.Label(mainframe, text='Number').grid(column=1, row=1, sticky=W)
        ttk.Label(mainframe, text='From Base').grid(column=2, row=1, sticky=W)
        ttk.Label(mainframe, text='To Base').grid(column=3, row=1, sticky=W)

        for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
        value_entry.focus()
        base_from_entry.focus()
        base_to_entry.focus()
        root.bind('<Return>', self.calculate)
        root.mainloop()

    def calculate(self, *args):
        try:
            number = self.value.get()
            from_base = int(self.base_from.get())
            to_base = int(self.base_to.get())
            self.result.set(Converter().convert(number=number, to_base=to_base, from_base=from_base))
        except ValueError:
            pass
