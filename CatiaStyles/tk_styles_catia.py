import tkinter as tk

class ButtonCatia(tk.Button):
    def __init__(self, master, type: str, text: str, command, width=7):
        super().__init__(master=master)
        self.type = type
        self.text = text
        self.command = command
        self.width = width
        self.apply_styles()
        self.bind("<Enter>", self._set_button_color_hover)
        self.bind("<Leave>", self._set_button_color_normal)

    def apply_styles(self): 
        self.configure(text = self.text)
        self.configure(relief=tk.RIDGE)
        self.configure(borderwidth=0.5)
        self.configure(font=("Roboto", 10))
        self.configure(width=self.width)
        self.configure(command=self.command)

        if self.type == 'blue':
            self.configure(activebackground = '#005686')
            self.configure(bg="#42A2DA")
            self.configure(activeforeground='#FFFFFF')
            self.configure(fg='#FFFFFF')
            self.configure(font=("Roboto", 10, "bold"))
        


    def _set_button_color_hover(self, event):
        if self.type == 'blue':
            event.widget.config(bg="#368EC4")

    def _set_button_color_normal(self, event):
        if self.type == 'blue':
            event.widget.config(bg="#42A2DA")


class CheckbuttonCatia(tk.Checkbutton):
    def __init__(self, master, text: str, state=False):
        super().__init__(master=master)
        self.text = text
        self.bind("<ButtonRelease-1>", self._set_checkbox_color)
        self.state = state
        self.configure(variable=self.state)
        self.configure(text=self.text)

    def _set_checkbox_color(self, event):
        if self.state:
            event.widget.config(selectcolor="#FFFFFF")
            self.state = False
        else:
            event.widget.config(selectcolor="#42A2DA")
            self.state = True



    


    


    
        