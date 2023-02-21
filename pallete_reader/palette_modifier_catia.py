import tkinter as tk
from tkinter import colorchooser
from tkinter import ttk

DATA_TO_CHANGE = dict()

class VerticalScrolledFrame(ttk.Frame):
    """A pure Tkinter scrollable frame that actually works!
    * Use the 'interior' attribute to place widgets inside the scrollable frame.
    * Construct and pack/place/grid normally.
    * This frame only allows vertical scrolling.
    """
    def __init__(self, parent, *args, **kw):
        ttk.Frame.__init__(self, parent, *args, **kw)

        # Create a canvas object and a vertical scrollbar for scrolling it.
        vscrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL)
        vscrollbar.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)
        canvas = tk.Canvas(self, bd=0, highlightthickness=0,
                           yscrollcommand=vscrollbar.set)
        canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=tk.TRUE)
        vscrollbar.config(command=canvas.yview)

        # Reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # Create a frame inside the canvas which will be scrolled with it.
        self.interior = interior = ttk.Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior,
                                           anchor=tk.NW)

        # Track changes to the canvas and frame width and sync them,
        # also updating the scrollbar.
        def _configure_interior(event):
            # Update the scrollbars to match the size of the inner frame.
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # Update the canvas's width to fit the inner frame.
                canvas.config(width=interior.winfo_reqwidth())
        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # Update the inner frame's width to fill the canvas.
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())
        canvas.bind('<Configure>', _configure_canvas)
        
        
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


class PaletteCollorSelector:
  def __init__(self, root, data_dict, palette_fields, palette_file):
    self.root = root
    self.data_dict = data_dict
    self.palette_fields = palette_fields
    self.palette_file = palette_file
    screen_width = root.winfo_screenwidth()
    screen_width = root.winfo_screenheight()
    screen_heigth = root.winfo_screenheight()
    center_x = int(screen_width/2 - 250)
    self.root.geometry(f"600x740+{center_x}+{50}")
    self.root.resizable(0, 0)

    self.root.title("Palette Color Selector")
    self.root.font=("Roboto", 10)
    self._create_widgets()
    

  def _create_widgets(self):
    self.file_label = tk.Label(self.root, text='Choose a palette field')
    self.file_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.EW)

    self.chosen_field = tk.StringVar(self.root)
    self.attribute_list = tk.Listbox(self.root, listvariable=self.chosen_field, activestyle='none',  highlightcolor='#B4B6BA', selectbackground='#42A2DA', height=30, width=40, relief='groove', border=0.5)
    [self.attribute_list.insert(tk.END, i) for i in self.palette_fields]
    self.attribute_list.grid(row=1, column=0, padx=10, pady=10, sticky=tk.N+tk.S)
    self.attribute_list.select_set(0) #This only sets focus on the first item.
    self.attribute_list.bind("<<ListboxSelect>>", func=self._draw_palette)
    self.attribute_list.select_set(0) #This only sets focus on the first item.

    scrollbar = tk.Scrollbar(self.root, command=self.attribute_list.yview)
    scrollbar.grid(row=1, column=0, padx=10, pady=0, sticky=tk.S + tk.N + tk.E)
    scrollbar.config(command = self.attribute_list.yview )

    self.attribute_list['yscrollcommand'] = scrollbar.set

    self.color_frame = tk.Frame(self.root)
    self.color_frame.grid(row=1, column=1, rowspan=100, columnspan=2, padx=10, pady=10, sticky=tk.N+tk.S)            
    self.start_palette_label = tk.Label(self.color_frame, text="Choose a field to explore palette")
    self.start_palette_label.grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky=tk.N)

    ok_button = ButtonCatia(self.root, type='blue', text="OK", command=self._write_new_pallete)
    ok_button.grid(row=102, column=1, padx=0, pady=10)

    cancel_button = ButtonCatia(self.root, type='gray', text="Cancel", command=self.root.destroy)
    cancel_button.grid(row=102, column=2, padx=10, pady=10)

  def _write_new_pallete(self):
    for row in range(1, int(self.palette_file.RowsNb + 1)):
      if row in DATA_TO_CHANGE.keys():
        self.palette_file.SetCell(row+1, 4, DATA_TO_CHANGE[row][0])
        print(DATA_TO_CHANGE[row])
    self.root.destroy()

  def _draw_palette(self, event):
    # print(self.data_dict)
    self.color_frame.destroy()
    field_name = self.attribute_list.get(self.attribute_list.curselection()[0])
    self.color_frame = VerticalScrolledFrame(self.root)
    self.color_frame.grid(row=1, column=1, columnspan=2, padx=5, pady=10, sticky=tk.N+tk.S+tk.E)
    # pixel = tk.PhotoImage(width=70, height=10)
    color_list = self.data_dict[field_name][:-1] if self.data_dict[field_name][-1][1] == '' else self.data_dict[field_name]
    is_numeric = self.data_dict[field_name][-1][1] == ''
    for i, value in enumerate(color_list):
        # print(value)
        color = value[1] if value[2] not in DATA_TO_CHANGE.keys() else DATA_TO_CHANGE[value[2]][0]
        text_label = f'{value[0]} -> {self.data_dict[field_name][i+1][0]}' if is_numeric else value[0]
        tk.Label(self.color_frame.interior, text=text_label, font=("Roboto", 8)).grid(row=i+1, column=1, padx=10, pady=1)
        tk.Button(self.color_frame.interior, name=f'color_button_{i}', command=lambda values=[i, value, field_name, self.data_dict[field_name][-1]]: self.get_color(values), 
                  bg=color, width=10, relief='flat', border=0).grid(row=i+1, column=2, padx=10, pady=1, sticky=tk.N)

  def get_color(self, values):
    color = colorchooser.askcolor()[1]
    tk.Button.nametowidget(self.color_frame, name=f'color_button_{values[0]}').config(bg=color)
    DATA_TO_CHANGE[values[1][2]] = [color]

    
temp_list = []
palette_data = []
palette_file = ekl.CreateSheet("GEOScience|STPM")
row_number = int(palette_file.RowsNb) + 1
column_number = int(palette_file.ColumnsNb) + 1
for row in range(1, row_number):
  for column in range(1, column_number):
    temp_list.append(palette_file.CellAsString(row, column))
  palette_data.append(temp_list)
  temp_list = []

data_dict = dict()
for i, row in enumerate(palette_data):
  if row[1] != '' and len(temp_list) == 0:
    temp_list.append([row[2], row[3], i+1])
    data_dict[str(row[1])] = temp_list
  elif row[1] == '':
    temp_list.append([row[2], row[3], i+1])
  else:
    temp_list = []
    temp_list.append([row[2], row[3], i+1])
    data_dict[str(row[1])] = temp_list

palette_fields = list(data_dict.keys())
    
root = tk.Tk()
app = PaletteCollorSelector(root, data_dict, palette_fields, palette_file)
root.mainloop()




    