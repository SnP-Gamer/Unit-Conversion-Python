#unit_converter.py

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

def length_conversion():
    units = {
        "m": 1,
        "km": 1000,
        "cm": 0.01,
        "mm": 0.001,
        "ft": 0.3048,
        "in": 0.0254,
        "yd": 0.9144,
        "mi": 1609.34
    }
    print("\nLength units available:")
    print(", ".join(sorted(units.keys())))
    
    value = get_float("Enter the length value you want to convert: ")
    from_unit = get_unit("Convert from (unit abbreviation): ", units)
    to_unit = get_unit("Convert to (unit abbreviation): ", units)

    meters = value * units[from_unit]
    result = meters / units[to_unit]
    print(f"{value} {from_unit} = {result:.2f} {to_unit}")

def weight_conversion():
    units = {
        "mg": 0.001,
        "g": 1,
        "kg": 1000,
        "oz": 28.3495,
        "lb": 453.592,
        "st": 6350.29  # stones
    }
    print("\nWeight units available:")
    print(", ".join(sorted(units.keys())))
    
    value = get_float("Enter the weight value you want to convert: ")
    from_unit = get_unit("Convert from (unit abbreviation): ", units)
    to_unit = get_unit("Convert to (unit abbreviation): ", units)

    grams = value * units[from_unit]
    result = grams / units[to_unit]
    print(f"{value} {from_unit} = {result:.2f} {to_unit}")

def temperature_conversion():
    units = {"c", "f", "k"}
    print("\nTemperature units available:")
    print("C (Celsius), F (Fahrenheit), K (Kelvin)")
    
    value = get_float("Enter the temperature value you want to convert: ")
    from_unit = get_unit("Convert from (C/F/K): ", units).upper()
    to_unit = get_unit("Convert to (C/F/K): ", units).upper()

    if from_unit == to_unit:
        print(f"{value} {from_unit} = {value:.2f} {to_unit}")
        return

    # Convert input to Celsius
    if from_unit == "F":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "K":
        celsius = value - 273.15
    else:
        celsius = value

    # Convert Celsius to target unit
    if to_unit == "F":
        result = celsius * 9 / 5 + 32
    elif to_unit == "K":
        result = celsius + 273.15
    else:
        result = celsius

    print(f"{value} {from_unit} = {result:.2f} {to_unit}")

def main():
    while True:
        print("\nUnit Converter Pro - Choose an option:")
        print("1. Length Conversion")
        print("2. Weight Conversion")
        print("3. Temperature Conversion")
        print("4. Exit")
        choice = input("Enter 1, 2, 3, or 4: ").strip()

        if choice == "1":
            length_conversion()
        elif choice == "2":
            weight_conversion()
        elif choice == "3":
            temperature_conversion()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()