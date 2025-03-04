"""Displays GUI on Windows OS"""
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
# from tkinter import font
from converter import Converter, Temperature


class GUI:
    def __init__(self):
        self.is_on = True
        """The encoding is set to allow future extensions to be compatible, font is kept as default for now"""
        self.uft_encode = "utf-8"
        self.font = ""
        self.root = tk.Tk()
        self.root.iconbitmap(r"Documents/Icon.ico")
        self.weight_units = ['Kilograms', 'Ounces', 'Pounds']
        self.distance_units = ['Miles', 'Nautical Miles', 'Yards', 'Feet', 'Kilometers', 'Hectometers', 'Meters',
                               'Centimeters', 'Millimeters', 'Inches']
        self.energy_units = ['Terajoules', 'Gigajoules', 'Megajoules', 'Kilojoules', 'Joules', 'Kilocalories',
                             'Calories']
        self.pressure_units = ['Atmospheres', 'Bars', 'Torr', 'Kilopascals', 'Pascals']
        self.conversion_choice = ""
        self.conversion_type_choice_frame = ttk.Frame(self.root)
        self.temp_choice_button = ttk.Button(self.conversion_type_choice_frame, text="Temperature")
        self.weight_choice_button = ttk.Button(self.conversion_type_choice_frame, text="Weight")
        self.distance_choice_button = ttk.Button(self.conversion_type_choice_frame, text="Distance")
        self.energy_choice_button = ttk.Button(self.conversion_type_choice_frame, text="Energy")
        self.pressure_choice_button = ttk.Button(self.conversion_type_choice_frame, text="Pressure")
        self.unit_choices_frame = ttk.Frame(self.root)
        self.from_unit = ""
        self.first_unit_label = ttk.Label(self.unit_choices_frame, text="First Unit")
        self.first_unit = ttk.Combobox(self.unit_choices_frame, values=[])
        self.to_unit = ""
        self.second_unit_label = ttk.Label(self.unit_choices_frame, text="Second Unit")
        self.second_unit = ttk.Combobox(self.unit_choices_frame, values=[])
        self.starting_accuracy = tk.StringVar()
        self.starting_accuracy.set("1")
        self.accuracy = 1
        self.choose_accuracy_label = ttk.Label(self.unit_choices_frame, text="Decimal places")
        self.choose_accuracy = ttk.Spinbox(self.unit_choices_frame, increment=1, from_=1, to=6,
                                           textvariable=self.starting_accuracy)
        self.result_label = ttk.Label(self.unit_choices_frame, text="The result is..")
        self.result_output = tk.Text(self.unit_choices_frame, height=1, width=15)
        self.convert_button = ttk.Button(self.root, text="Convert")
        self.user_value_label = ttk.Label(self.unit_choices_frame, text="Enter Value")
        self.reset_button = ttk.Button(self.root, text="Reset")
        self.user_value = ttk.Entry(self.unit_choices_frame)
        self.user_value_stored = 0.0
        self.converted_value = 0.0
        self.canvas_window_frame = ttk.Frame(self.root)
        self.logo_canvas = tk.Canvas(self.canvas_window_frame)
        self.logo_img = tk.PhotoImage(file=r"Documents/FinalGuiLogo.png")
        self.s = ttk.Style()

    def convert_button_method(self):
        try:
            self.user_value_stored = float(self.user_value.get())
            self.check_user_inputs()
            if -9000001 < self.user_value_stored < 9000001:
                self.result_output.delete('1.0', 'end')

                if value := Temperature.convert_temperature(
                    self.from_unit, self.to_unit, self.user_value_stored
                ):
                    self.converted_value = value

                if self.from_unit == 'Kilograms' and self.to_unit == 'Ounces':
                    self.converted_value = Converter.convert_kilogram_to_ounces(self.user_value_stored)
                elif self.from_unit == 'Kilograms' and self.to_unit == 'Pounds':
                    self.converted_value = Converter.convert_kilograms_to_pounds(self.user_value_stored)
                elif self.from_unit == 'Ounces' and self.to_unit == 'Kilograms':
                    self.converted_value = Converter.convert_ounces_to_kilograms(self.user_value_stored)
                elif self.from_unit == 'Ounces' and self.to_unit == 'Pounds':
                    self.converted_value = Converter.convert_ounces_to_pounds(self.user_value_stored)
                elif self.from_unit == 'Pounds' and self.to_unit == 'Kilograms':
                    self.converted_value = Converter.convert_pounds_to_kilograms(self.user_value_stored)
                elif self.from_unit == 'Pounds' and self.to_unit == 'Ounces':
                    self.converted_value = Converter.convert_pounds_to_ounces(self.user_value_stored)
                elif self.from_unit == 'Miles' and self.to_unit == 'Nautical Miles':
                    self.converted_value = Converter.convert_miles_to_nautical_miles(self.user_value_stored)
                elif self.from_unit == 'Miles' and self.to_unit == 'Yards':
                    self.converted_value = Converter.convert_miles_to_yards(self.user_value_stored)
                elif self.from_unit == 'Miles' and self.to_unit == 'Feet':
                    self.converted_value = Converter.convert_miles_to_feet(self.user_value_stored)
                elif self.from_unit == 'Miles' and self.to_unit == 'Kilometers':
                    self.converted_value = Converter.convert_miles_to_kilometers(self.user_value_stored)
                elif self.from_unit == 'Miles' and self.to_unit == 'Hectometers':
                    self.converted_value = Converter.convert_miles_to_hectometers(self.user_value_stored)
                elif self.from_unit == 'Miles' and self.to_unit == 'Meters':
                    self.converted_value = Converter.convert_miles_to_meters(self.user_value_stored)
                elif self.from_unit == 'Miles' and self.to_unit == 'Centimeters':
                    self.converted_value = Converter.convert_miles_to_centimeters(self.user_value_stored)
                elif self.from_unit == 'Miles' and self.to_unit == 'Millimeters':
                    self.converted_value = Converter.convert_miles_to_millimeters(self.user_value_stored)
                elif self.from_unit == 'Miles' and self.to_unit == 'Inches':
                    self.converted_value = Converter.convert_miles_to_inches(self.user_value_stored)
                elif self.from_unit == 'Nautical Miles' and self.to_unit == 'Miles':
                    self.converted_value = Converter.convert_nautical_miles_to_miles(self.user_value_stored)
                elif self.from_unit == 'Nautical Miles' and self.to_unit == 'Yards':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_nautical_miles_to_yards(self.user_value_stored)
                elif self.from_unit == 'Nautical Miles' and self.to_unit == 'Feet':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_nautical_miles_to_feet(self.user_value_stored)
                elif self.from_unit == 'Nautical Miles' and self.to_unit == 'Kilometers':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_nautical_miles_to_kilometers(self.user_value_stored)
                elif self.from_unit == 'Nautical Miles' and self.to_unit == 'Hectometers':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_nautical_miles_to_hectometers(self.user_value_stored)
                elif self.from_unit == 'Nautical Miles' and self.to_unit == 'Meters':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_nautical_miles_to_meters(self.user_value_stored)
                elif self.from_unit == 'Nautical Miles' and self.to_unit == 'Centimeters':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_nautical_miles_to_centimeters(self.user_value_stored)
                elif self.from_unit == 'Nautical Miles' and self.to_unit == 'Millimeters':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_nautical_miles_to_millimeters(self.user_value_stored)
                elif self.from_unit == 'Nautical Miles' and self.to_unit == 'Inches':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_nautical_miles_to_inches(self.user_value_stored)
                elif self.from_unit == 'Yards' and self.to_unit == 'Miles':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_yards_to_miles(self.user_value_stored)
                elif self.from_unit == 'Yards' and self.to_unit == 'Nautical Miles':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_yards_to_nautical_miles(self.user_value_stored)
                elif self.from_unit == 'Yards' and self.to_unit == 'Feet':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_yards_to_feet(self.user_value_stored)
                elif self.from_unit == 'Yards' and self.to_unit == 'Kilometers':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_yards_to_kilometers(self.user_value_stored)
                elif self.from_unit == 'Yards' and self.to_unit == 'Hectometers':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_yards_to_hectometers(self.user_value_stored)
                elif self.from_unit == 'Yards' and self.to_unit == 'Meters':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_yards_to_meters(self.user_value_stored)
                elif self.from_unit == 'Yards' and self.to_unit == 'Centimeters':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_yards_to_centimeters(self.user_value_stored)
                elif self.from_unit == 'Yards' and self.to_unit == 'Millimeters':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_yards_to_millimeters(self.user_value_stored)
                elif self.from_unit == 'Yards' and self.to_unit == 'Inches':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_yards_to_inches(self.user_value_stored)
                elif self.from_unit == 'Feet' and self.to_unit == 'Miles':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_feet_to_miles(self.user_value_stored)
                elif self.from_unit == 'Feet' and self.to_unit == 'Nautical Miles':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_feet_to_nautical_miles(self.user_value_stored)
                elif self.from_unit == 'Feet' and self.to_unit == 'Yards':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_feet_to_yards(self.user_value_stored)
                elif self.from_unit == 'Feet' and self.to_unit == 'Kilometers':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_feet_to_kilometers(self.user_value_stored)
                elif self.from_unit == 'Feet' and self.to_unit == 'Hectometers':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_feet_to_hectometers(self.user_value_stored)
                elif self.from_unit == 'Feet' and self.to_unit == 'Meters':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_feet_to_meters(self.user_value_stored)
                elif self.from_unit == 'Feet' and self.to_unit == 'Centimeters':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_feet_to_centimeters(self.user_value_stored)
                elif self.from_unit == 'Feet' and self.to_unit == 'Millimeters':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_feet_to_millimeters(self.user_value_stored)
                elif self.from_unit == 'Feet' and self.to_unit == 'Inches':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_feet_to_inches(self.user_value_stored)
                elif self.from_unit == 'Kilometers' and self.to_unit == 'Miles':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_kilometers_to_miles(self.user_value_stored)
                elif self.from_unit == 'Kilometers' and self.to_unit == 'Nautical Miles':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_kilometers_to_nautical_miles(self.user_value_stored)
                elif self.from_unit == 'Kilometers' and self.to_unit == 'Yards':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_kilometers_to_yards(self.user_value_stored)
                elif self.from_unit == 'Kilometers' and self.to_unit == 'Hectometers':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_kilometers_to_hectometers(self.user_value_stored)
                elif self.from_unit == 'Kilometers' and self.to_unit == 'Meters':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_kilometers_to_meters(self.user_value_stored)
                elif self.from_unit == 'Kilometers' and self.to_unit == 'Centimeters':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_kilometers_to_centimeters(self.user_value_stored)
                elif self.from_unit == 'Kilometers' and self.to_unit == 'Millimeters':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_kilometers_to_millimeters(self.user_value_stored)
                elif self.from_unit == 'Kilometers' and self.to_unit == 'Inches':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_kilometers_to_inches(self.user_value_stored)
                elif self.from_unit == 'Hectometers' and self.to_unit == 'Miles':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_hectometers_to_miles(self.user_value_stored)
                elif self.from_unit == 'Hectometers' and self.to_unit == 'Nautical Miles':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_hectometers_to_nautical_miles(self.user_value_stored)
                elif self.from_unit == 'Hectometers' and self.to_unit == 'Yards':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_hectometers_to_yards(self.user_value_stored)
                elif self.from_unit == 'Hectometers' and self.to_unit == 'Feet':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_hectometers_to_yards(self.user_value_stored)
                elif self.from_unit == 'Hectometers' and self.to_unit == 'Kilometers':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_hectometers_to_kilometers(self.user_value_stored)
                elif self.from_unit == 'Hectometers' and self.to_unit == 'Meters':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_hectometers_to_meters(self.user_value_stored)
                elif self.from_unit == 'Hectometers' and self.to_unit == 'Centimeters':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_hectometers_to_centimeters(self.user_value_stored)
                elif self.from_unit == 'Hectometers' and self.to_unit == 'Millimeters':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_hectometers_to_millimeters(self.user_value_stored)
                elif self.from_unit == 'Hectometers' and self.to_unit == 'Inches':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_hectometers_to_inches(self.user_value_stored)
                elif self.from_unit == 'Meters' and self.to_unit == 'Miles':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_meters_to_miles(self.user_value_stored)
                elif self.from_unit == 'Meters' and self.to_unit == 'Nautical Miles':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_meters_to_nautical_miles(self.user_value_stored)
                elif self.from_unit == 'Meters' and self.to_unit == 'Yards':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_meters_to_yards(self.user_value_stored)
                elif self.from_unit == 'Meters' and self.to_unit == 'Feet':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_meters_to_feet(self.user_value_stored)
                elif self.from_unit == 'Meters' and self.to_unit == 'Kilometers':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_meters_to_kilometers(self.user_value_stored)
                elif self.from_unit == 'Meters' and self.to_unit == 'Hectometers':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_meters_to_hectometers(self.user_value_stored)
                elif self.from_unit == 'Meters' and self.to_unit == 'Centimeters':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_meters_to_centimeters(self.user_value_stored)
                elif self.from_unit == 'Meters' and self.to_unit == 'Millimeters':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_meters_to_millimeters(self.user_value_stored)
                elif self.from_unit == 'Meters' and self.to_unit == 'Inches':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_meters_to_inches(self.user_value_stored)
                elif self.from_unit == 'Centimeters' and self.to_unit == 'Miles':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_centimeters_to_miles(self.user_value_stored)
                elif self.from_unit == 'Centimeters' and self.to_unit == 'Nautical Miles':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_centimeters_to_nautical_miles(self.user_value_stored)
                elif self.from_unit == 'Centimeters' and self.to_unit == 'Yards':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_centimeters_to_yards(self.user_value_stored)
                elif self.from_unit == 'Centimeters' and self.to_unit == 'Feet':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_centimeters_to_feet(self.user_value_stored)
                elif self.from_unit == 'Centimeters' and self.to_unit == 'Kilometers':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_centimeters_to_kilometers(self.user_value_stored)
                elif self.from_unit == 'Centimeters' and self.to_unit == 'Hectometers':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_centimeters_to_hectometers(self.user_value_stored)
                elif self.from_unit == 'Centimeters' and self.to_unit == 'Meters':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_centimeters_to_meters(self.user_value_stored)
                elif self.from_unit == 'Centimeters' and self.to_unit == 'Millimeters':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_centimeters_to_millimeters(self.user_value_stored)
                elif self.from_unit == 'Centimeters' and self.to_unit == 'Inches':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_centimeters_to_inches(self.user_value_stored)
                elif self.from_unit == 'Millimeters' and self.to_unit == 'Miles':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_millimeters_to_miles(self.user_value_stored)
                elif self.from_unit == 'Millimeters' and self.to_unit == 'Nautical Miles':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_millimeters_to_nautical_miles(self.user_value_stored)
                elif self.from_unit == 'Millimeters' and self.to_unit == 'Yards':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_millimeters_to_yards(self.user_value_stored)
                elif self.from_unit == 'Millimeters' and self.to_unit == 'Feet':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_millimeters_to_feet(self.user_value_stored)
                elif self.from_unit == 'Millimeters' and self.to_unit == 'Kilometers':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_millimeters_to_kilometers(self.user_value_stored)
                elif self.from_unit == 'Millimeters' and self.to_unit == 'Hectometers':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_millimeters_to_hectometers(self.user_value_stored)
                elif self.from_unit == 'Millimeters' and self.to_unit == 'Meters':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_millimeters_to_meters(self.user_value_stored)
                elif self.from_unit == 'Millimeters' and self.to_unit == 'Centimeters':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_millimeters_to_centimeters(self.user_value_stored)
                elif self.from_unit == 'Millimeters' and self.to_unit == 'Inches':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_millimeters_to_inches(self.user_value_stored)
                elif self.from_unit == 'Inches' and self.to_unit == 'Miles':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_inches_to_miles(self.user_value_stored)
                elif self.from_unit == 'Inches' and self.to_unit == 'Nautical Miles':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_inches_to_nautical_miles(self.user_value_stored)
                elif self.from_unit == 'Inches' and self.to_unit == 'Yards':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_inches_to_yards(self.user_value_stored)
                elif self.from_unit == 'Inches' and self.to_unit == 'Feet':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_inches_to_feet(self.user_value_stored)
                elif self.from_unit == 'Inches' and self.to_unit == 'Kilometers':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_inches_to_kilometers(self.user_value_stored)
                elif self.from_unit == 'Inches' and self.to_unit == 'Hectometers':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_inches_to_hectometers(self.user_value_stored)
                elif self.from_unit == 'Inches' and self.to_unit == 'Meters':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_inches_to_meters(self.user_value_stored)
                elif self.from_unit == 'Inches' and self.to_unit == 'Centimeters':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_inches_to_centimeters(self.user_value_stored)
                elif self.from_unit == 'Inches' and self.to_unit == 'Millimeters':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_inches_to_millimeters(self.user_value_stored)
                elif self.from_unit == 'Atmospheres' and self.to_unit == 'Bars':
                    Converter.user_value = self.user_value_stored
                    self.converted_value = Converter.convert_atmospheres_to_bars(self.user_value_stored)
                elif self.from_unit == 'Atmospheres' and self.to_unit == 'Torr':
                    self.converted_value = Converter.convert_atmospheres_to_torr(self.user_value_stored)
                elif self.from_unit == 'Atmospheres' and self.to_unit == 'Kilopascals':
                    self.converted_value = Converter.convert_atmospheres_to_kilopascals(self.user_value_stored)
                elif self.from_unit == 'Atmospheres' and self.to_unit == 'Pascals':
                    self.converted_value = Converter.convert_atmospheres_to_pascals(self.user_value_stored)
                elif self.from_unit == 'Bars' and self.to_unit == 'Atmospheres':
                    self.converted_value = Converter.convert_bars_to_atmospheres(self.user_value_stored)
                elif self.from_unit == 'Bars' and self.to_unit == 'Torr':
                    self.converted_value = Converter.convert_bars_to_torr(self.user_value_stored)
                elif self.from_unit == 'Bars' and self.to_unit == 'Kilopascals':
                    self.converted_value = Converter.convert_bars_to_kilopascals(self.user_value_stored)
                elif self.from_unit == 'Bars' and self.to_unit == 'Pascals':
                    self.converted_value = Converter.convert_bars_to_pascals(self.user_value_stored)
                elif self.from_unit == 'Torr' and self.to_unit == 'Atmospheres':
                    self.converted_value = Converter.convert_torr_to_atmospheres(self.user_value_stored)
                elif self.from_unit == 'Torr' and self.to_unit == 'Bars':
                    self.converted_value = Converter.convert_torr_to_bars(self.user_value_stored)
                elif self.from_unit == 'Torr' and self.to_unit == 'Kilopascals':
                    self.converted_value = Converter.convert_torr_to_kilopascals(self.user_value_stored)
                elif self.from_unit == 'Torr' and self.to_unit == 'Pascals':
                    self.converted_value = Converter.convert_torr_to_pascals(self.user_value_stored)
                elif self.from_unit == 'Kilopascals' and self.to_unit == 'Atmospheres':
                    self.converted_value = Converter.convert_kilopascals_to_atmospheres(self.user_value_stored)
                elif self.from_unit == 'Kilopascals' and self.to_unit == 'Bars':
                    self.converted_value = Converter.convert_kilopascals_to_bars(self.user_value_stored)
                elif self.from_unit == 'Kilopascals' and self.to_unit == 'Torr':
                    self.converted_value = Converter.convert_kilopascals_to_torr(self.user_value_stored)
                elif self.from_unit == 'Kilopascals' and self.to_unit == 'Pascals':
                    self.converted_value = Converter.convert_kilopascals_to_pascals(self.user_value_stored)
                elif self.from_unit == 'Pascals' and self.to_unit == 'Atmospheres':
                    self.converted_value = Converter.convert_pascals_to_atmospheres(self.user_value_stored)
                elif self.from_unit == 'Pascals' and self.to_unit == 'Bars':
                    self.converted_value = Converter.convert_pascals_to_bars(self.user_value_stored)
                elif self.from_unit == 'Pascals' and self.to_unit == 'Torr':
                    self.converted_value = Converter.convert_pascals_to_torr(self.user_value_stored)
                elif self.from_unit == 'Pascals' and self.to_unit == 'Kilopascals':
                    self.converted_value = Converter.convert_pascals_to_kilopascals(self.user_value_stored)
                elif self.from_unit == 'Terajoules' and self.to_unit == 'Gigajoules':
                    self.converted_value = Converter.convert_terajoules_to_gigajoules(self.user_value_stored)
                elif self.from_unit == 'Terajoules' and self.to_unit == 'Megajoules':
                    self.converted_value = Converter.convert_terajoules_to_megajoules(self.user_value_stored)
                elif self.from_unit == 'Terajoules' and self.to_unit == 'Kilojoules':
                    self.converted_value = Converter.convert_terajoules_to_kilojoules(self.user_value_stored)
                elif self.from_unit == 'Terajoules' and self.to_unit == 'Joules':
                    self.converted_value = Converter.convert_terajoules_to_joules(self.user_value_stored)
                elif self.from_unit == 'Terajoules' and self.to_unit == 'Kilocalories':
                    self.converted_value = Converter.convert_terajoules_to_kilocalories(self.user_value_stored)
                elif self.from_unit == 'Terajoules' and self.to_unit == 'Calories':
                    self.converted_value = Converter.convert_terajoules_to_calories(self.user_value_stored)
                elif self.from_unit == 'Gigajoules' and self.to_unit == 'Terajoules':
                    self.converted_value = Converter.convert_gigajoules_to_terajoules(self.user_value_stored)
                elif self.from_unit == 'Gigajoules' and self.to_unit == 'Megajoules':
                    self.converted_value = Converter.convert_gigajoules_to_megajoules(self.user_value_stored)
                elif self.from_unit == 'Gigajoules' and self.to_unit == 'Kilojoules':
                    self.converted_value = Converter.convert_gigajoules_to_kilojoules(self.user_value_stored)
                elif self.from_unit == 'Gigajoules' and self.to_unit == 'Joules':
                    self.converted_value = Converter.convert_gigajoules_to_joules(self.user_value_stored)
                elif self.from_unit == 'Gigajoules' and self.to_unit == 'Kilocalories':
                    self.converted_value = Converter.convert_gigajoules_to_kilocalories(self.user_value_stored)
                elif self.from_unit == 'Gigajoules' and self.to_unit == 'Calories':
                    self.converted_value = Converter.convert_gigajoules_to_calories(self.user_value_stored)
                elif self.from_unit == 'Megajoules' and self.to_unit == 'Terajoules':
                    self.converted_value = Converter.convert_megajoules_to_terajoules(self.user_value_stored)
                elif self.from_unit == 'Megajoules' and self.to_unit == 'Gigajoules':
                    self.converted_value = Converter.convert_megajoules_to_gigajoules(self.user_value_stored)
                elif self.from_unit == 'Megajoules' and self.to_unit == 'Kilojoules':
                    self.converted_value = Converter.convert_megajoules_to_kilojoules(self.user_value_stored)
                elif self.from_unit == 'Megajoules' and self.to_unit == 'Joules':
                    self.converted_value = Converter.convert_megajoules_to_joules(self.user_value_stored)
                elif self.from_unit == 'Megajoules' and self.to_unit == 'Kilocalories':
                    self.converted_value = Converter.convert_megajoules_to_kilocalories(self.user_value_stored)
                elif self.from_unit == 'Megajoules' and self.to_unit == 'Calories':
                    self.converted_value = Converter.convert_megajoules_to_calories(self.user_value_stored)
                elif self.from_unit == 'Kilojoules' and self.to_unit == 'Terajoules':
                    self.converted_value = Converter.convert_kilojoules_to_terajoules(self.user_value_stored)
                elif self.from_unit == 'Kilojoules' and self.to_unit == 'Gigajoules':
                    self.converted_value = Converter.convert_kilojoules_to_gigajoules(self.user_value_stored)
                elif self.from_unit == 'Kilojoules' and self.to_unit == 'Megajoules':
                    self.converted_value = Converter.convert_kilojoules_to_megajoules(self.user_value_stored)
                elif self.from_unit == 'Kilojoules' and self.to_unit == 'Joules':
                    self.converted_value = Converter.convert_kilojoules_to_joules(self.user_value_stored)
                elif self.from_unit == 'Kilojoules' and self.to_unit == 'Kilocalories':
                    self.converted_value = Converter.convert_kilojoules_to_kilocalories(self.user_value_stored)
                elif self.from_unit == 'Kilojoules' and self.to_unit == 'Calories':
                    self.converted_value = Converter.convert_kilojoules_to_calories(self.user_value_stored)
                elif self.from_unit == 'Joules' and self.to_unit == 'Terajoules':
                    self.converted_value = Converter.convert_joules_to_terajoules(self.user_value_stored)
                elif self.from_unit == 'Joules' and self.to_unit == 'Gigajoules':
                    self.converted_value = Converter.convert_joules_to_gigajoules(self.user_value_stored)
                elif self.from_unit == 'Joules' and self.to_unit == 'Megajoules':
                    self.converted_value = Converter.convert_joules_to_megajoules(self.user_value_stored)
                elif self.from_unit == 'Joules' and self.to_unit == 'Kilojoules':
                    self.converted_value = Converter.convert_joules_to_kilojoules(self.user_value_stored)
                elif self.from_unit == 'Joules' and self.to_unit == 'Kilocalories':
                    self.converted_value = Converter.convert_joules_to_kilocalories(self.user_value_stored)
                elif self.from_unit == 'Joules' and self.to_unit == 'Calories':
                    self.converted_value = Converter.convert_joules_to_calories(self.user_value_stored)
                elif self.from_unit == 'Kilocalories' and self.to_unit == 'Terajoules':
                    self.converted_value = Converter.convert_kilocalories_to_terajoules(self.user_value_stored)
                elif self.from_unit == 'Kilocalories' and self.to_unit == 'Gigajoules':
                    self.converted_value = Converter.convert_kilocalories_to_gigajoules(self.user_value_stored)
                elif self.from_unit == 'Kilocalories' and self.to_unit == 'Megajoules':
                    self.converted_value = Converter.convert_kilocalories_to_megajoules(self.user_value_stored)
                elif self.from_unit == 'Kilocalories' and self.to_unit == 'Kilojoules':
                    self.converted_value = Converter.convert_kilocalories_to_kilojoules(self.user_value_stored)
                elif self.from_unit == 'Kilocalories' and self.to_unit == 'Joules':
                    self.converted_value = Converter.convert_kilocalories_to_joules(self.user_value_stored)
                elif self.from_unit == 'Kilocalories' and self.to_unit == 'Calories':
                    self.converted_value = Converter.convert_kilocalories_to_calories(self.user_value_stored)
                elif self.from_unit == 'Calories' and self.to_unit == 'Terajoules':
                    self.converted_value = Converter.convert_calories_to_terajoules(self.user_value_stored)
                elif self.from_unit == 'Calories' and self.to_unit == 'Gigajoules':
                    self.converted_value = Converter.convert_calories_to_gigajoules(self.user_value_stored)
                elif self.from_unit == 'Calories' and self.to_unit == 'Megajoules':
                    self.converted_value = Converter.convert_calories_to_megajoules(self.user_value_stored)
                elif self.from_unit == 'Calories' and self.to_unit == 'Kilojoules':
                    self.converted_value = Converter.convert_calories_to_kilojoules(self.user_value_stored)
                elif self.from_unit == 'Calories' and self.to_unit == 'Joules':
                    self.converted_value = Converter.convert_calories_to_joules(self.user_value_stored)
                elif self.from_unit == 'Calories' and self.to_unit == 'Kilocalories':
                    self.converted_value = Converter.convert_calories_to_kilocalories(self.user_value_stored)
                self.converted_value = round(self.converted_value, self.accuracy)
                print(self.converted_value)
                self.remove_error_highlights()
                self.user_output()
        except ValueError:
            self.check_user_inputs()

    def user_output(self):
        self.result_output.insert('1.0', str(self.converted_value))
        return self.converted_value

    def show_temp_options(self):
        self.first_unit.config(values=Temperature.units)
        self.second_unit.config(values=Temperature.units)

    def show_weight_options(self):
        self.first_unit.config(values=self.weight_units)
        self.second_unit.config(values=self.weight_units)

    def show_energy_options(self):
        self.first_unit.config(values=self.energy_units)
        self.second_unit.config(values=self.energy_units)

    def show_distance_options(self):
        self.first_unit.config(values=self.distance_units)
        self.second_unit.config(values=self.distance_units)

    def show_pressure_options(self):
        self.first_unit.config(values=self.pressure_units)
        self.second_unit.config(values=self.pressure_units)

    def set_first_unit(self, event):
        self.from_unit = event.widget.get()
        return self.from_unit

    def set_second_unit(self, event):
        self.to_unit = event.widget.get()
        return self.to_unit

    def get_accuracy(self):
        self.accuracy = int(self.choose_accuracy.get())
        return self.accuracy

    def check_user_inputs(self):
        if self.user_value_stored > 9000001:
            self.user_value.config(foreground="red")
            messagebox.showerror(title="Error", message="value is too high", detail="Enter a number from -9,000,000 to"
                                                                                    " 9,000,000")
        if self.user_value_stored < -9000001:
            self.user_value.config(foreground="red")
            messagebox.showerror(title="Error", message="value is too low", detail="Enter a number from -9,000,000 to"
                                                                                   " 9,000,000")
        if self.user_value_stored == 0:
            self.user_value.config(foreground="red")
            messagebox.showerror(title="Error", message="Enter a numerical value")
        if self.from_unit == "" or self.to_unit == "":
            messagebox.showerror(title="Error", message="Select conversion units!")
        if self.from_unit == self.to_unit:
            self.first_unit.config(foreground="red")
            messagebox.showerror(title="Error", message="Conversion units are identical")

    def remove_error_highlights(self):
        self.user_value.config(foreground="")
        self.first_unit.config(foreground="")
        return self.user_value, self.first_unit

    def reset_function(self):
        self.get_accuracy()
        self.result_output.delete('1.0', 'end')
        self.first_unit.set('')
        self.second_unit.set('')
        self.user_value_stored = 0.0
        self.user_value.delete(0, 'end')
        return self.result_output

    def style_widgets(self):
        self.root.config(bg="#7fadf7")
        self.s.configure('TFrame', background='#7fadf7')

    def place_gui_elements(self):
        self.conversion_type_choice_frame.grid(column=0, row=0, pady=5, padx=5, ipady=5, ipadx=5)
        self.temp_choice_button.grid(column=0, row=0, padx=1, pady=1)
        self.weight_choice_button.grid(column=0, row=1, padx=1, pady=1)
        self.distance_choice_button.grid(column=0, row=2, padx=1, pady=1)
        self.energy_choice_button.grid(column=0, row=3, padx=1, pady=1)
        self.pressure_choice_button.grid(column=1, row=0, padx=1, pady=1)
        self.unit_choices_frame.grid(column=1, row=0, pady=5, padx=5, ipady=5, ipadx=5)
        self.first_unit_label.grid(column=0, row=0, sticky="w", padx=5, pady=1)
        self.first_unit.grid(column=1, row=0, pady=1)
        self.second_unit_label.grid(column=0, row=1, sticky="w", padx=5, pady=1)
        self.second_unit.grid(column=1, row=1, sticky="w", pady=1)
        self.choose_accuracy_label.grid(column=0, row=2, padx=5, pady=1)
        self.choose_accuracy.grid(column=1, row=2, sticky="w", pady=1)
        self.user_value_label.grid(column=0, row=3, sticky="w", padx=5, pady=1)
        self.user_value.grid(column=1, row=3, sticky="w", pady=1)
        self.result_label.grid(column=0, row=4, sticky="w", padx=5, pady=1)
        self.result_output.grid(column=1, row=4, sticky="w", pady=1)
        self.convert_button.grid(column=1, row=3, pady=5, padx=5, ipady=5, ipadx=5)
        self.reset_button.grid(column=0, row=3, pady=5, padx=5, ipady=5, ipadx=5)
        self.canvas_window_frame.grid(column=0, row=4, columnspan=2, pady=5, padx=5, ipady=5, ipadx=5)
        self.logo_canvas.grid(columnspan=2, column=0, row=5)
        self.logo_canvas.create_image(0, 0, anchor='nw', image=self.logo_img)

    def initialise_gui_elements(self):
        self.temp_choice_button.config(command=self.show_temp_options)
        self.weight_choice_button.config(command=self.show_weight_options)
        self.distance_choice_button.config(command=self.show_distance_options)
        self.energy_choice_button.config(command=self.show_energy_options)
        self.pressure_choice_button.config(command=self.show_pressure_options)
        self.convert_button.config(command=self.convert_button_method)
        self.first_unit.bind("<<ComboboxSelected>>", self.set_first_unit)
        self.second_unit.bind("<<ComboboxSelected>>", self.set_second_unit)
        self.choose_accuracy.config(command=self.get_accuracy)
        self.reset_button.config(command=self.reset_function)
        self.logo_canvas.config(width=300, height=300, bd=0)

    def display_gui(self):
        self.root.title("Converter Application")
        self.root.geometry('500x500')
        self.root.resizable(False, False)
        self.root.columnconfigure(0, weight=1)
        self.style_widgets()
        self.place_gui_elements()
        self.initialise_gui_elements()
        self.root.mainloop()
        self.is_on = False
        return self.is_on
