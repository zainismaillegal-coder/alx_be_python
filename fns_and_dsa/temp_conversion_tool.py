FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        temperature = float(input("Enter the temperature to convert: "))
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "F":
        result = convert_to_celsius(temperature)
        print(f"{temperature}°F is {result}°C")
    elif unit == "C":
        result = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {result}°F")
    else:
        raise ValueError("Invalid unit. Please enter 'C' or 'F'.")

if __name__ == "__main__":
    main()
