#unit_converter.py, made on android using pydroid3 with ai assisstance 

def get_unit(prompt, valid_units):
    while True:
        unit = input(prompt).strip().lower()
        if unit in valid_units:
            return unit
        print(f"Invalid unit. Please enter one of: {', '.join(sorted(valid_units))}")

def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")

unit_names = {
    # Length
    "mm": "millimeter", "cm": "centimeter", "m": "meter", "km": "kilometer",
    "in": "inch", "ft": "foot", "yd": "yard", "mi": "mile", "nmi": "nautical mile",

    # Weight
    "mg": "milligram", "g": "gram", "kg": "kilogram", "tonne": "metric ton",
    "oz": "ounce", "lb": "pound", "st": "stone", "ton": "US short ton",

    # Volume
    "ml": "milliliter", "l": "liter", "m3": "cubic meter",
    "metric pt": "metric pint", "metric qt": "metric quart", "metric gal": "metric gallon",
    "tsp": "teaspoon", "tbsp": "tablespoon", "fl oz": "fluid ounce",
    "cup": "cup", "pt": "US pint", "qt": "US quart", "gal": "US gallon",

    # Speed
    "m/s": "meters per second", "km/h": "kilometers per hour",
    "mph": "miles per hour", "knot": "nautical miles per hour",

    # Temperature
    "c": "Celsius", "f": "Fahrenheit", "k": "Kelvin",

    # Data
    "bit": "bit", "kb": "kilobit", "mb": "megabit", "gb": "gigabit",
    "tb": "terabit", "b": "bit",
    "B": "byte", "KB": "kilobyte", "MB": "megabyte", "GB": "gigabyte", "TB": "terabyte",

    # Pressure
    "pa": "pascal", "kpa": "kilopascal", "bar": "bar",
    "psi": "pound per square inch", "atm": "atmosphere", "torr": "torr",

    # Time
    "s": "second", "min": "minute", "h": "hour",
    "d": "day", "wk": "week", "mo": "month (30.44d avg)", "yr": "year"
}

def length_conversion():
    units = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000,
        "in": 0.0254,
        "ft": 0.3048,
        "yd": 0.9144,
        "mi": 1609.344,
        "nmi": 1852
    }
    print("\nLength units available:")
    for key in sorted(units.keys()):
        print(f"  {key} = {unit_names.get(key, 'Unknown')}")

    value = get_float("Enter the length value you want to convert: ")
    from_unit = get_unit("Convert from (unit abbreviation): ", units)
    to_unit = get_unit("Convert to (unit abbreviation): ", units)

    meters = value * units[from_unit]
    result = meters / units[to_unit]
    print(f"{value} {from_unit} = {result:.4f} {to_unit}")

def weight_conversion():
    units = {
        "mg": 0.001,
        "g": 1,
        "kg": 1000,
        "oz": 28.3495,
        "lb": 453.592,
        "st": 6350.29,  # stones
        "tonne": 1_000_000,
        "ton": 907184.74  # US short ton
    }
    print("\nWeight units available:")
    for key in sorted(units.keys()):
        print(f"  {key} = {unit_names.get(key, 'Unknown')}")

    value = get_float("Enter the weight value you want to convert: ")
    from_unit = get_unit("Convert from (unit abbreviation): ", units)
    to_unit = get_unit("Convert to (unit abbreviation): ", units)

    grams = value * units[from_unit]
    result = grams / units[to_unit]
    print(f"{value} {from_unit} = {result:.4f} {to_unit}")

def temperature_conversion():
    units = {"c", "f", "k"}
    print("\nTemperature units available:")
    for key in sorted(units):
        print(f"  {key} = {unit_names.get(key, 'Unknown')}")

    value = get_float("Enter the temperature value you want to convert: ")
    from_unit = get_unit("Convert from (C/F/K): ", units).lower()
    to_unit = get_unit("Convert to (C/F/K): ", units).lower()

    if from_unit == to_unit:
        print(f"{value} {from_unit.upper()} = {value:.2f} {to_unit.upper()}")
        return

    # Convert input to Celsius
    if from_unit == "f":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "k":
        celsius = value - 273.15
    else:
        celsius = value

    # Convert Celsius to target unit
    if to_unit == "f":
        result = celsius * 9 / 5 + 32
    elif to_unit == "k":
        result = celsius + 273.15
    else:
        result = celsius

    print(f"{value} {from_unit.upper()} = {result:.2f} {to_unit.upper()}")

def volume_conversion():
    units = {
        "ml": 0.001,
        "l": 1,
        "m3": 1000,
        "metric pt": 0.5,
        "metric qt": 1,
        "metric gal": 4,
        "tsp": 0.00492892,
        "tbsp": 0.0147868,
        "fl oz": 0.0295735,
        "cup": 0.24,
        "pt": 0.473176,  # US pint
        "qt": 0.946353,  # US quart
        "gal": 3.78541   # US gallon
    }
    print("\nVolume units available:")
    for key in sorted(units.keys()):
        print(f"  {key} = {unit_names.get(key, 'Unknown')}")

    value = get_float("Enter the volume value you want to convert: ")
    from_unit = get_unit("Convert from (unit abbreviation): ", units)
    to_unit = get_unit("Convert to (unit abbreviation): ", units)

    liters = value * units[from_unit]
    result = liters / units[to_unit]
    print(f"{value} {from_unit} = {result:.4f} {to_unit}")

def speed_conversion():
    units = {
        "m/s": 1,
        "km/h": 0.277778,
        "mph": 0.44704,
        "knot": 0.514444
    }
    print("\nSpeed units available:")
    for key in sorted(units.keys()):
        print(f"  {key} = {unit_names.get(key, 'Unknown')}")

    value = get_float("Enter the speed value you want to convert: ")
    from_unit = get_unit("Convert from (unit abbreviation): ", units)
    to_unit = get_unit("Convert to (unit abbreviation): ", units)

    meters_per_sec = value * units[from_unit]
    result = meters_per_sec / units[to_unit]
    print(f"{value} {from_unit} = {result:.4f} {to_unit}")

def data_conversion():
    units = {
        "bit": 1,
        "kb": 1e3,
        "mb": 1e6,
        "gb": 1e9,
        "tb": 1e12,
        "b": 1,  # bit alias lowercase
        "B": 8,
        "KB": 8e3,
        "MB": 8e6,
        "GB": 8e9,
        "TB": 8e12
    }
    print("\nData units available:")
    for key in sorted(units.keys(), key=str.lower):
        print(f"  {key} = {unit_names.get(key, 'Unknown')}")

    value = get_float("Enter the data size to convert: ")
    from_unit = get_unit("Convert from: ", units)
    to_unit = get_unit("Convert to: ", units)

    bits = value * units[from_unit]
    result = bits / units[to_unit]
    print(f"{value} {from_unit} = {result:.4f} {to_unit}")

def pressure_conversion():
    units = {
        "pa": 1,
        "kpa": 1000,
        "bar": 100000,
        "psi": 6894.76,
        "atm": 101325,
        "torr": 133.322
    }
    print("\nPressure units available:")
    for key in sorted(units.keys()):
        print(f"  {key} = {unit_names.get(key, 'Unknown')}")

    value = get_float("Enter the pressure value to convert: ")
    from_unit = get_unit("Convert from: ", units)
    to_unit = get_unit("Convert to: ", units)

    pascals = value * units[from_unit]
    result = pascals / units[to_unit]
    print(f"{value} {from_unit} = {result:.4f} {to_unit}")

def time_conversion():
    units = {
        "s": 1,
        "min": 60,
        "h": 3600,
        "d": 86400,
        "wk": 604800,
        "mo": 2629800,   # average month (30.44 days)
        "yr": 31557600   # average year (365.25 days)
    }
    print("\nTime units available:")
    for key in sorted(units.keys()):
        print(f"  {key} = {unit_names.get(key, 'Unknown')}")

    value = get_float("Enter the time duration to convert: ")
    from_unit = get_unit("Convert from: ", units)
    to_unit = get_unit("Convert to: ", units)

    seconds = value * units[from_unit]
    result = seconds / units[to_unit]
    print(f"{value} {from_unit} = {result:.4f} {to_unit}")

def main():
    while True:
        print("\nUnit Converter Pro - Choose an option:")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        print("4. Volume")
        print("5. Speed")
        print("6. Data")
        print("7. Pressure")
        print("8. Time")
        print("9. Exit")
        choice = input("Enter 1–9: ").strip()

        if choice == "1":
            length_conversion()
        elif choice == "2":
            weight_conversion()
        elif choice == "3":
            temperature_conversion()
        elif choice == "4":
            volume_conversion()
        elif choice == "5":
            speed_conversion()
        elif choice == "6":
            data_conversion()
        elif choice == "7":
            pressure_conversion()
        elif choice == "8":
            time_conversion()
        elif choice == "9":
            print("Goodbye, Sir!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 9.")

if __name__ == "__main__":
      main()