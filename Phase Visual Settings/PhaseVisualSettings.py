
import win32com.client
CATIA = win32com.client.Dispatch('CATIA.Application')
myProdService = CATIA.ActiveEditor.GetService('PLMProductService')
prdSessionService = CATIA.GetSessionService('ProductSessionService')
oObjSelection = CATIA.ActiveEditor.Selection
myEntities = myProdService.EditedContent

oInputObjectType = ['HybridBody']
strStatus = oObjSelection.SelectElement(oInputObjectType, 'Select a Pit Phase', False)
oSelectedElement = oObjSelection.Item(1)

HybridBody = oSelectedElement.Value
PhaseHybridBodies = HybridBody.HybridBodies

import tkinter as tk
from tkinter import colorchooser
from tkinter import ttk

class Form:
    def __init__(self, master):
        self.master = master
        self.master.title("Form")

        # Toe color label and color chooser
        tk.Label(self.master, text="Toe color").grid(row=0, column=0, padx=10, pady=10)
        self.toe_color = tk.Button(self.master, text="Choose color" ,command=self.get_toe_color)
        self.toe_color.grid(row=0, column=1, padx=10, pady=10)

        # Crest color label and color chooser
        tk.Label(self.master, text="Crest color").grid(row=1, column=0, padx=10, pady=10)
        self.crest_color = tk.Button(self.master, text="Choose color", command=self.get_crest_color)
        self.crest_color.grid(row=1, column=1, padx=10, pady=10)

        # Toe line width label and drop-down menu
        tk.Label(self.master, text="Toe Line width").grid(row=2, column=0, padx=10, pady=10)
        self.toe_width = ttk.Combobox(self.master, values=[1, 2, 3, 4, 5], state="readonly")
        self.toe_width.current(0)
        self.toe_width.grid(row=2, column=1, padx=10, pady=10)

        # Crest line width label and drop-down menu
        tk.Label(self.master, text="Crest Line width").grid(row=3, column=0, padx=10, pady=10)
        self.crest_width = ttk.Combobox(self.master, values=[1, 2, 3, 4, 5], state="readonly")
        self.crest_width.current(1)
        self.crest_width.grid(row=3, column=1, padx=10, pady=10)

        # Toe line type label and drop-down menu
        tk.Label(self.master, text="Toe line type").grid(row=4, column=0, padx=10, pady=10)
        self.toe_type = ttk.Combobox(self.master, values=["Solid", "Dashed", "Dotted"], state="readonly",)
        self.toe_type.current(1)
        self.toe_type.grid(row=4, column=1, padx=10, pady=10)

        # Crest line type label and drop-down menu
        tk.Label(self.master, text="Crest line type").grid(row=5, column=0, padx=10, pady=10)
        self.crest_type = ttk.Combobox(self.master, values=["Solid", "Dashed", "Dotted"], state="readonly")
        self.crest_type.current(0)
        self.crest_type.grid(row=5, column=1, padx=10, pady=10)

        # OK and Cancel
        # OK and Cancel buttons
        self.ok_button = tk.Button(self.master, text="OK", command=self.print_params)
        self.ok_button.grid(row=6, column=0, padx=10, pady=10)
        self.cancel_button = tk.Button(self.master, text="Cancel", command=self.master.quit)
        self.cancel_button.grid(row=6, column=1, padx=10, pady=10)
        self.line_dict = {"Dotted": 6, "Solid": 1, "Dashed": 3}

    def get_toe_color(self):
        color = colorchooser.askcolor()[1]
        self.toe_color.config(bg=color)

    def get_crest_color(self):
        color = colorchooser.askcolor()[1]
        self.crest_color.config(bg=color)

    def hex_to_rgb(self, hex):
        rgb = []
        for i in (0, 2, 4):
            decimal = int(hex[i:i+2], 16)
            rgb.append(decimal)
        return tuple(rgb)

    def print_params(self):
        self.toe_color = self.toe_color.cget("bg")
        self.crest_color = self.crest_color.cget("bg")
        self.toe_width = self.toe_width.get()
        self.crest_width = self.crest_width.get()
        self.toe_type = self.toe_type.get()
        self.crest_type = self.crest_type.get()
        self.master.destroy()

root = tk.Tk()
form = Form(root)
root.mainloop()
toe_color = form.hex_to_rgb(form.toe_color[1:])
crest_color = form.hex_to_rgb(form.crest_color[1:])

properties = oObjSelection.VisProperties
for i in range(1, PhaseHybridBodies.Count + 1):
    BenchHybridBodies = PhaseHybridBodies.Item(i).HybridBodies
    for k in range(1, BenchHybridBodies.Count + 1):
        BenchHybridShapes = BenchHybridBodies.Item(k).HybridShapes
        for j in range(1, BenchHybridShapes.Count + 1):
            if ('Crest'in BenchHybridShapes.Item(j).Name) or ('Ramp Contour'in BenchHybridShapes.Item(j).Name):
                oObjSelection.Add(BenchHybridShapes.Item(j))
                properties.SetRealColor(crest_color[0], crest_color[1], crest_color[2], 0)
                properties.SetVisibleLineType(form.line_dict[form.crest_type], 0)
                properties.SetRealWidth(int(form.crest_width), 0)
                oObjSelection.Clear()
            else:
                oObjSelection.Add(BenchHybridShapes.Item(j))
                properties.SetRealColor(toe_color[0], toe_color[1], toe_color[2], 0)
                properties.SetVisibleLineType(form.line_dict[form.toe_type], 0)
                properties.SetRealWidth(int(form.toe_width), 0)
                oObjSelection.Clear()
