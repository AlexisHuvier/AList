from tkinter import Toplevel, ttk, StringVar


class StringChooser:
    def __init__(self, parent, title, message, callback, *possibility):
        self.callback = callback
        self.top = Toplevel(parent)
        self.top.title(title)

        label = ttk.Label(self.top, text=message)
        label.pack(padx=10, pady=10)

        self.var = StringVar(self.top)
        self.var.set(possibility[0])
        chooser = ttk.OptionMenu(self.top, self.var, possibility[0], *possibility)
        chooser["width"] = 30
        chooser.pack(padx=10, pady=10)

        btn = ttk.Button(self.top, text="Valider", width=20, command=self.validate)
        btn.pack(padx=10, pady=10)

    def validate(self):
        self.top.quit()
        self.callback(self.var.get())
