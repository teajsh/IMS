try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk

from tkcalendar import Calendar, DateEntry

def example1():
    def print_sel():
        print(cal.selection_get())

    top = tk.Toplevel(root)

    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                    year=2023, month=4, day=5)
    cal.pack(fill="both", expand=False)
    ttk.Button(top, text="ok", command=print_sel).pack()

def enterdate():
    top = tk.Toplevel(root)

    ttk.Label(top, text='Choose date').pack(padx=10, pady=10)

    cal = DateEntry(top, width=12, background='white',
                    foreground='white', borderwidth=2)
    cal.pack(padx=30, pady=30)

root = tk.Tk()
s = ttk.Style(root)
s.theme_use('clam')

ttk.Button(root, text='Calendar', command=example1).pack(padx=100, pady=100)
ttk.Button(root, text='DateEntry', command=enterdate).pack(padx=100, pady=100)

root.mainloop()