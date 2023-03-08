import tkinter as tk
from tkinter import ttk

class DrillProgramGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Drill Program GUI")
        # self.geometry("400x200")
        
        # Add tabs
        tabControl = ttk.Notebook(self)
        self.drillhole_params_tab = ttk.Frame(tabControl, padding=20)
        self.charging_tab = ttk.Frame(tabControl, padding=20)
        self.drill_pattern_tab = ttk.Frame(tabControl, padding=20)
        self.sequence_pattern_tab = ttk.Frame(tabControl, padding=20)
        self.reports_tab = ttk.Frame(tabControl, padding=20)
        
        tabControl.add(self.drillhole_params_tab, text="Drillhole Parameters")
        tabControl.add(self.charging_tab, text="Charging")
        tabControl.add(self.drill_pattern_tab, text="Drill Pattern")
        tabControl.add(self.sequence_pattern_tab, text="Sequence Pattern")
        tabControl.add(self.reports_tab, text="Reports")
        tabControl.grid(row=0, column=0, rowspan=3)
        self.buttons = ttk.Frame(self)
        self.buttons.grid(row=3, column=0)
        
        # Drill pattern tab
        # drill_pattern_label = ttk.Label(self.drill_pattern_tab, text="Here will be a chosen boundary name label")
        # drill_pattern_label.grid(row=0, column=0)
        
        # drill_grid_label = ttk.Label(self.drill_pattern_tab, text="Drill grid")
        # drill_grid_label.grid(row=1, column=0)
        # drill_grid_entry = ttk.Entry(self.drill_pattern_tab)
        # drill_grid_entry.grid(row=1, column=1)
        # drill_grid_x_label = ttk.Label(self.drill_pattern_tab, text="x")
        # drill_grid_x_label.grid(row=1, column=2)
        # drill_grid_x_entry = ttk.Entry(self.drill_pattern_tab)
        # drill_grid_x_entry.grid(row=1, column=3)
        
        # drill_pattern_label = ttk.Label(self.drill_pattern_tab, text="Drill pattern")
        # drill_pattern_label.grid(row=2, column=0)
        # drill_pattern_options = ["Diamond", "Rectangle"]
        # drill_pattern_dropdown = ttk.Combobox(self.drill_pattern_tab, values=drill_pattern_options)
        # drill_pattern_dropdown.grid(row=2, column=1)
        
        # drill_direction_label = ttk.Label(self.drill_pattern_tab, text="Drill direction (azimuth)")
        # drill_direction_label.grid(row=3, column=0)
        # drill_direction_entry = ttk.Entry(self.drill_pattern_tab)
        # drill_direction_entry.grid(row=3, column=1)
        # drill_direction_degrees_label = ttk.Label(self.drill_pattern_tab, text="degrees")
        # drill_direction_degrees_label.grid(row=3, column=2)
        for tab in [self.drillhole_params_tab, self.charging_tab, self.drill_pattern_tab, self.sequence_pattern_tab, self.reports_tab]:    
            tab.columnconfigure(0, weight=1)
            tab.columnconfigure(1, weight=3)
            tab.columnconfigure(2, weight=1)
        
        # # Drillhole parameters tab
        drillhole_floor_label = ttk.Label(self.drillhole_params_tab, text="Drillhole floor elevation")
        drillhole_floor_label.grid(row=0, column=0, padx=5, pady=10, sticky=tk.W)
        drillhole_floor_entry = ttk.Entry(self.drillhole_params_tab)
        drillhole_floor_entry.grid(row=0, column=1, padx=5, pady=10)
        drillhole_floor_meters_label = ttk.Label(self.drillhole_params_tab, text="m")
        drillhole_floor_meters_label.grid(row=0, column=2, padx=5, pady=10, sticky=tk.W)
        
        drillhole_diameter_label = ttk.Label(self.drillhole_params_tab, text="Drillhole diameter")
        drillhole_diameter_label.grid(row=1, column=0, padx=5, pady=10, sticky=tk.W)
        drillhole_diameter_entry = ttk.Entry(self.drillhole_params_tab)
        drillhole_diameter_entry.grid(row=1, column=1, padx=5, pady=10)
        drillhole_diameter_mm_label = ttk.Label(self.drillhole_params_tab, text="mm")
        drillhole_diameter_mm_label.grid(row=1, column=2, padx=5, pady=10, sticky=tk.W)
        
        drillhole_angle_label = ttk.Label(self.drillhole_params_tab, text="Drillhole angle")
        drillhole_angle_label.grid(row=2, column=0, padx=5, pady=10, sticky=tk.W)
        drillhole_angle_entry = ttk.Entry(self.drillhole_params_tab)
        drillhole_angle_entry.grid(row=2, column=1, padx=5, pady=10)
        drillhole_angle_degrees_label = ttk.Label(self.drillhole_params_tab, text="degrees")
        drillhole_angle_degrees_label.grid(row=2, column=2, padx=5, pady=10, sticky=tk.W)
        
        drillhole_azimuth_label = ttk.Label(self.drillhole_params_tab, text="Drillhole azimuth")
        drillhole_azimuth_label.grid(row=3, column=0, padx=5, pady=10, sticky=tk.W)
        drillhole_azimuth_entry = ttk.Entry(self.drillhole_params_tab)
        drillhole_azimuth_entry.grid(row=3, column=1, padx=5, pady=10)
        drillhole_azimuth_degrees_label = ttk.Label(self.drillhole_params_tab, text="degrees")
        drillhole_azimuth_degrees_label.grid(row=3, column=2, padx=5, pady=10, sticky=tk.W)
        
        # # Charging tab
        explosives_weight_label = ttk.Label(self.charging_tab, text="Explosives weight")
        explosives_weight_label.grid(row=0, column=0, padx=5, pady=10, sticky=tk.W)
        explosives_weight_entry = ttk.Entry(self.charging_tab)
        explosives_weight_entry.grid(row=0, column=1, padx=5, pady=10)
        explosives_weight_kg_label = ttk.Label(self.charging_tab, text="kg")
        explosives_weight_kg_label.grid(row=0, column=2, padx=5, pady=10, sticky=tk.W)
        
        explosives_density_label = ttk.Label(self.charging_tab, text="Explosives density")
        explosives_density_label.grid(row=1, column=0, padx=5, pady=10, sticky=tk.W)
        explosives_density_entry = ttk.Entry(self.charging_tab)
        explosives_density_entry.grid(row=1, column=1, padx=5, pady=10)
        explosives_density_gsm3_label = ttk.Label(self.charging_tab, text="g/sm3")
        explosives_density_gsm3_label.grid(row=1, column=2, padx=5, pady=10, sticky=tk.W)
        
        booster_diameter_label = ttk.Label(self.charging_tab, text="Booster weight")
        booster_diameter_label.grid(row=2, column=0, padx=5, pady=10, sticky=tk.W)
        booster_diameter_entry = ttk.Entry(self.charging_tab)
        booster_diameter_entry.grid(row=2, column=1, padx=5, pady=10)
        booster_diameter_mm_label = ttk.Label(self.charging_tab, text="g")
        booster_diameter_mm_label.grid(row=2, column=2, padx=5, pady=10, sticky=tk.W)
        
        booster_offset_label = ttk.Label(self.charging_tab, text="Booster offset")
        booster_offset_label.grid(row=3, column=0, padx=5, pady=10, sticky=tk.W)
        options = ["350", "400", "450", "900"]
        selected = tk.StringVar()
        selected.set(options[0])
        booster_offset_entry = ttk.OptionMenu(self.charging_tab, selected, *options)
        booster_offset_entry.grid(row=3, column=1, padx=5, pady=10, sticky=tk.W+tk.E)
        booster_offset_m_label = ttk.Label(self.charging_tab, text="m")
        booster_offset_m_label.grid(row=3, column=2, padx=5, pady=10, sticky=tk.W)

        downhole_delay_label = ttk.Label(self.charging_tab, text="Downhole delay")
        downhole_delay_label.grid(row=4, column=0, padx=5, pady=10, sticky=tk.W)
        options2 = ["200", "400", "600", "800", "1000"]
        selected2 = tk.StringVar()
        selected2.set(options[0])
        downhole_delay_entry = ttk.OptionMenu(self.charging_tab, selected2, *options2)
        # downhole_delay_entry.config(width=15)
        downhole_delay_entry.grid(row=4, column=1, padx=5, pady=10, sticky=tk.W+tk.E)
        downhole_delay_m_label = ttk.Label(self.charging_tab, text="ms")
        downhole_delay_m_label.grid(row=4, column=2, padx=5, pady=10, sticky=tk.W)
        
        stemming_length_label = ttk.Label(self.charging_tab, text="Stemming length")
        stemming_length_label.grid(row=5, column=0, padx=5, pady=10, sticky=tk.W)
        stemming_length_entry = ttk.Entry(self.charging_tab)
        stemming_length_entry.grid(row=5, column=1, padx=5, pady=10)
        stemming_length_m_label = ttk.Label(self.charging_tab, text="m")
        stemming_length_m_label.grid(row=5, column=2, padx=5, pady=10, sticky=tk.W)
        
        # # Sequence pattern tab
        # downhole_delay_label = ttk.Label(self.sequence_pattern_tab, text="Down-hole delay")
        # downhole_delay_label.pack(pady=10)
        # downhole_delay_entry = ttk.Entry(self.sequence_pattern_tab)
        # downhole_delay_entry.pack()
        # downhole_delay_ms_label = ttk.Label(self.sequence_pattern_tab, text="ms")
        # downhole_delay_ms_label.pack()
        
        # surface_delay_label = ttk.Label(self.sequence_pattern_tab, text="Surface delay")
        # surface_delay_label.pack(pady=10)
        # surface_delay_entry = ttk.Entry(self.sequence_pattern_tab)
        # surface_delay_entry.pack()
        # surface_delay_ms_label = ttk.Label(self.sequence_pattern_tab, text="ms")
        # surface_delay_ms_label.pack()
        
        # # Reports tab
        # block_drilling_totals_checkbutton = ttk.Checkbutton(self.reports_tab, text="Block drilling totals")
        # block_drilling_totals_checkbutton.pack(pady=10)
        
        # block_charge_totals_checkbutton = ttk.Checkbutton(self.reports_tab, text="Block charge totals")
        # block_charge_totals_checkbutton.pack(pady=10)
        
        # sequencing_checkbutton = ttk.Checkbutton(self.reports_tab, text="Sequencing")
        # sequencing_checkbutton.pack(pady=10)
        
        # # Add buttons
        # button_frame = ttk.Frame(self.buttons)
        # button_frame.grid(row=2, column=3)

        ok_button = ttk.Button(self.buttons, text="OK", command=self.on_ok_button_click)
        ok_button.grid(row=4, column=3, padx=5, pady=10)

        cancel_button = ttk.Button(self.buttons, text="Cancel", command=self.on_cancel_button_click)
        cancel_button.grid(row=4, column=4, padx=5, pady=10)

#         light_gray = "#e0e0e0"
#         blue = "#2196f3"

#         style = ttk.Style()
#         style.theme_create("MyStyle", parent="alt", settings={
#         "TNotebook": {"configure": {"tabmargins": [0, 5, 0, 0]}},
#         "TNotebook.Tab": {"configure": {"padding": [10, 5], "font": ("TkDefaultFont", 11), "background": "light gray"}, "sticky": "wns", "map": {"background": [("selected", "blue")], "foreground": [("selected", "white")]}},
#         "TFrame": {"configure": {"background": "light gray"}},
#         "TLabel": {"configure": {"font": ("TkDefaultFont", 11), "background": "light gray"}},
#         "TEntry": {"configure": {"font": ("TkDefaultFont", 11)}},
#         "TCombobox": {"configure": {"font": ("TkDefaultFont", 11)}},
#         "TButton": {"configure": {"font": ("TkDefaultFont", 11)}},
# })
#         style.theme_use("MyStyle")
#         style.configure("TNotebook", background="#e0e0e0")
#         style.configure("TNotebook.Tab", background=blue, foreground="#000000")
#         style.map("TNotebook.Tab", background=[("selected", "#ffffff")], foreground=[("selected", "#000000")])

    def on_ok_button_click(self):
        # TODO: Implement OK button functionality
        pass

    def on_cancel_button_click(self):
        self.root.destroy()

app = DrillProgramGUI()
app.mainloop()

