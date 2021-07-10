from tkinter import ttk, Canvas


class ScrollFrame(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.canvas = Canvas(self, borderwidth=0)
        self.viewport = ttk.Frame(self.canvas, width=kwargs["width"])
        self.vsb = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas_window = self.canvas.create_window((0, 0), window=self.viewport, anchor="nw", tags="self.viewport")

        self.viewport.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<Configure>", self.on_canvas_configure)
        self.bind("<Enter>", self.bind_mousewheel)
        self.bind("<Leave>", self.unbind_mousewheel)

        self.on_frame_configure(None)

    def bind_mousewheel(self, evt):
        # Windows
        self.canvas.bind_all("<MouseWheel>", self.on_canvas_mousewheel)

        # Linux
        self.canvas.bind_all("<Button-4>", self.on_canvas_mousewheel)
        self.canvas.bind_all("<Button-5>", self.on_canvas_mousewheel)

    def unbind_mousewheel(self, evt):
        # Windows
        self.canvas.unbind_all("<MouseWheel>")

        # Linux
        self.canvas.unbind_all("<Button-4>")
        self.canvas.unbind_all("<Button-5>")

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event):
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_window, width=canvas_width)

    def on_canvas_mousewheel(self, event):
        if self.canvas.winfo_exists():
            if event.num == 5 or event.delta == -120:
                self.canvas.yview_scroll(1, "units")
            if event.num == 4 or event.delta == 120:
                self.canvas.yview_scroll(-1, "units")
        else:
            self.unbind_mousewheel(None)
