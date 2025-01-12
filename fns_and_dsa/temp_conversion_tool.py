FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    try:
        temperature = int(input("Enter the temperature to convert: "))
        unit_of_measurement = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

        if unit_of_measurement == 'F':
            converted = convert_to_celsius(temperature)
            print(f"{temperature}{chr(176)}F is {converted}{chr(176)}C")
        elif  unit_of_measurement == 'C':
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}{chr(176)}C is {converted}{chr(176)}F")
        else:
            print("Invalid input. Goodbye!")
    except ValueError:
        print("Error. Temperature should be a number. Goodbye!")

if __name__=="__main__":
    main()