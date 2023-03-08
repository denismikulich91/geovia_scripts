import tkinter as tk
from tkinter import ttk

class DrillProgramGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Drill Program GUI")
        
        BoosterListOfChildren=root.Query("Feature","x.Name.Search('booster')>=0")
        self.booster = ListOfChildren.GetItem(1)
        self.boost_param =booster.Query("AdvisorParameterSet", "").GetItem(1)
        
        #Tie list to the name, otherwise it gets reorder-sensitive!!!
        StemmingListOfChildren=root.Query("Feature","x.Name.Search('stemming')>=0")
        self.stemming = StemmingListOfChildren.GetItem(1)
        self.stemming_param =stemming.Query("AdvisorParameterSet", "").GetItem(2)
        
        DrillholeListOfChildren=root.Query("Feature","x.Name.Search('drillhole')>=0")
        self.drillhole = DrillholeListOfChildren.GetItem(1)
        self.drillhole_param =self.drillhole.Query("BodyFeature", "").GetItem(1)
        self.drillhole_param = self.drillhole_param.Query("AdvisorParameterSet", "").GetItem(1)
        
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

        for tab in [self.drillhole_params_tab, self.charging_tab, self.drill_pattern_tab, self.sequence_pattern_tab, self.reports_tab]:    
            tab.columnconfigure(0, weight=1)
            tab.columnconfigure(1, weight=3)
            tab.columnconfigure(2, weight=1)
        
        # # Drillhole parameters tab
        self.drillhole_floor_label = ttk.Label(self.drillhole_params_tab, text="Drillhole floor elevation")
        self.drillhole_floor_label.grid(row=0, column=0, padx=5, pady=10, sticky=tk.W)
        self.drillhole_floor_entry = ttk.Entry(self.drillhole_params_tab)
        self.drillhole_floor_entry.insert(0, str(self.drillhole_param.GetAttributeReal("elevation")))
        self.drillhole_floor_entry.grid(row=0, column=1, padx=5, pady=10, sticky=tk.W+tk.E)
        self.drillhole_floor_meters_label = ttk.Label(self.drillhole_params_tab, text="m")
        self.drillhole_floor_meters_label.grid(row=0, column=2, padx=5, pady=10, sticky=tk.W)
        
        self.drillhole_diameter_label = ttk.Label(self.drillhole_params_tab, text="Drillhole diameter")
        self.drillhole_diameter_label.grid(row=1, column=0, padx=5, pady=10, sticky=tk.W)
        self.drillhole_diameter_entry = ttk.Entry(self.drillhole_params_tab)
        self.drillhole_diameter_entry.insert(0, str(self.drillhole_param.GetAttributeReal("diameter")))
        self.drillhole_diameter_entry.grid(row=1, column=1, padx=5, pady=10, sticky=tk.W+tk.E)
        self.drillhole_diameter_mm_label = ttk.Label(self.drillhole_params_tab, text="mm")
        self.drillhole_diameter_mm_label.grid(row=1, column=2, padx=5, pady=10, sticky=tk.W)
        
        self.drillhole_angle_label = ttk.Label(self.drillhole_params_tab, text="Drillhole angle")
        self.drillhole_angle_label.grid(row=2, column=0, padx=5, pady=10, sticky=tk.W)
        self.drillhole_angle_entry = ttk.Entry(self.drillhole_params_tab)
        self.drillhole_angle_entry.insert(0, str(self.drillhole_param.GetAttributeReal("angle")))
        self.drillhole_angle_entry.grid(row=2, column=1, padx=5, pady=10, sticky=tk.W+tk.E)
        self.drillhole_angle_degrees_label = ttk.Label(self.drillhole_params_tab, text="degrees")
        self.drillhole_angle_degrees_label.grid(row=2, column=2, padx=5, pady=10, sticky=tk.W)
        
        self.drillhole_azimuth_label = ttk.Label(self.drillhole_params_tab, text="Drillhole azimuth")
        self.drillhole_azimuth_label.grid(row=3, column=0, padx=5, pady=10, sticky=tk.W)
        self.drillhole_azimuth_entry = ttk.Entry(self.drillhole_params_tab)
        self.drillhole_azimuth_entry.insert(0, str(self.drillhole_param.GetAttributeReal("azimuth")))
        self.drillhole_azimuth_entry.grid(row=3, column=1, padx=5, pady=10, sticky=tk.W+tk.E)
        self.drillhole_azimuth_degrees_label = ttk.Label(self.drillhole_params_tab, text="degrees")
        self.drillhole_azimuth_degrees_label.grid(row=3, column=2, padx=5, pady=10, sticky=tk.W)
        
        # # Charging tab
        self.explosives_weight_label = ttk.Label(self.charging_tab, text="Explosives weight")
        self.explosives_weight_label.grid(row=0, column=0, padx=5, pady=10, sticky=tk.W)
        self.explosives_weight_entry = ttk.Entry(self.charging_tab)
        self.explosives_weight_entry.insert(0, str(self.drillhole_param.GetAttributeReal("explosive_weight")))
        self.explosives_weight_entry.grid(row=0, column=1, padx=5, pady=10, sticky=tk.W+tk.E)
        self.explosives_weight_kg_label = ttk.Label(self.charging_tab, text="kg")
        self.explosives_weight_kg_label.grid(row=0, column=2, padx=5, pady=10, sticky=tk.W)
        
        self.explosives_density_label = ttk.Label(self.charging_tab, text="Explosives density")
        self.explosives_density_label.grid(row=1, column=0, padx=5, pady=10, sticky=tk.W)
        self.explosives_density_entry = ttk.Entry(self.charging_tab)
        self.explosives_density_entry.insert(0, str(self.drillhole_param.GetAttributeReal("explosive_sg")))
        self.explosives_density_entry.grid(row=1, column=1, padx=5, pady=10, sticky=tk.W+tk.E)
        self.explosives_density_gsm3_label = ttk.Label(self.charging_tab, text="g/sm3")
        self.explosives_density_gsm3_label.grid(row=1, column=2, padx=5, pady=10, sticky=tk.W)
        
        self.booster_weigth_label = ttk.Label(self.charging_tab, text="Booster weight")
        options = ["350", "400", "450", "900"]
        self.selected = tk.StringVar()
        self.booster_weigth_label.grid(row=2, column=0, padx=5, pady=10, sticky=tk.W)
        # TODO Set up default value
        
        self.booster_weigth_entry = ttk.OptionMenu(self.charging_tab, self.selected, str(self.boost_param.GetAttributeReal("booster_weight")), *options)
        self.booster_weigth_entry.grid(row=2, column=1, padx=5, pady=10, sticky=tk.W+tk.E)
        self.booster_weigth_g_label = ttk.Label(self.charging_tab, text="g")
        self.booster_weigth_g_label.grid(row=2, column=2, padx=5, pady=10, sticky=tk.W)
        
        self.booster_offset_label = ttk.Label(self.charging_tab, text="Booster offset")
        self.booster_offset_label.grid(row=3, column=0, padx=5, pady=10, sticky=tk.W)
        self.booster_offset_entry = ttk.Entry(self.charging_tab)
        self.booster_offset_entry.insert(0, str(self.boost_param.GetAttributeReal("gap_below")))
        self.booster_offset_entry.grid(row=3, column=1, padx=5, pady=10, sticky=tk.W+tk.E)
        self.booster_offset_m_label = ttk.Label(self.charging_tab, text="m")
        self.booster_offset_m_label.grid(row=3, column=2, padx=5, pady=10, sticky=tk.W)

        self.downhole_delay_label = ttk.Label(self.charging_tab, text="Downhole delay")
        self.downhole_delay_label.grid(row=4, column=0, padx=5, pady=10, sticky=tk.W)
        options2 = ["200", "400", "600", "800", "1000"]
        self.selected2 = tk.StringVar()
        self.downhole_delay_entry = ttk.OptionMenu(self.charging_tab, self.selected2, str(self.boost_param.GetAttributeReal("downhole_delay")*1000), *options2)
        self.downhole_delay_entry.grid(row=4, column=1, padx=5, pady=10, sticky=tk.W+tk.E)
        self.downhole_delay_m_label = ttk.Label(self.charging_tab, text="ms")
        self.downhole_delay_m_label.grid(row=4, column=2, padx=5, pady=10, sticky=tk.W)
        
        self.stemming_length_label = ttk.Label(self.charging_tab, text="Stemming length")
        self.stemming_length_label.grid(row=5, column=0, padx=5, pady=10, sticky=tk.W)
        self.stemming_length_entry = ttk.Entry(self.charging_tab)
        self.stemming_length_entry.insert(0, str(self.stemming_param.GetAttributeReal("stemming_heigth")))
        self.stemming_length_entry.grid(row=5, column=1, padx=5, pady=10, sticky=tk.W+tk.E)
        self.stemming_length_m_label = ttk.Label(self.charging_tab, text="m")
        self.stemming_length_m_label.grid(row=5, column=2, padx=5, pady=10, sticky=tk.W)

        ok_button = ttk.Button(self.buttons, text="OK", command=self.on_ok_button_click)
        ok_button.grid(row=4, column=3, padx=5, pady=10)

        cancel_button = ttk.Button(self.buttons, text="Cancel", command=self.on_cancel_button_click)
        cancel_button.grid(row=4, column=4, padx=5, pady=10)

    def on_ok_button_click(self):
        #Initial data from user:
        azimuth_gui = float(self.drillhole_azimuth_entry.get())
        angle_gui = float(self.drillhole_angle_entry.get())
        elevation_gui = float(self.drillhole_floor_entry.get())
        diameter_gui = float(self.drillhole_diameter_entry.get())
        explosive_sg_gui = float(self.explosives_density_entry.get())
        explosive_weight_gui = float(self.explosives_weight_entry.get())
        booster_weight_gui = float(self.selected.get())
        gap_below_gui = float(self.booster_offset_entry.get())
        #Input should be in ms, output into app in s
        downhole_delay_gui = float(self.selected2.get())/1000
        stemming_heigth_gui = float(self.stemming_length_entry.get())
        root=ekl.GetEditorRoots("VPMReference").GetItem(1)

        #Booster settings
        self.boost_param.SetAttributeReal("booster_weight", booster_weight_gui)
        self.boost_param.SetAttributeReal("gap_below", gap_below_gui)
        self.boost_param.SetAttributeReal("downhole_delay", downhole_delay_gui)
        self.booster.Update()

        #Stemming settings
        self.stemming_param.SetAttributeReal("stemming_heigth", stemming_heigth_gui)
        self.stemming.Update()

        #Drillhole and explosive settings
        self.drillhole_param.SetAttributeReal("azimuth", azimuth_gui)
        self.drillhole_param.SetAttributeReal("angle", angle_gui)
        self.drillhole_param.SetAttributeReal("elevation", elevation_gui)
        self.drillhole_param.SetAttributeReal("diameter", diameter_gui)
        self.drillhole_param.SetAttributeReal("explosive_sg", explosive_sg_gui)
        self.drillhole_param.SetAttributeReal("explosive_weight", explosive_weight_gui)
        self.drillhole.Update()
        self.destroy()

    def on_cancel_button_click(self):
        self.destroy()

app = DrillProgramGUI()
app.mainloop()

