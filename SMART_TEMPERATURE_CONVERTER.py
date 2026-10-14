#Smart temperature converter
input_temp_in_celsius = float(input("Enter the temperature in Celsius: "))
fahrenheit = (input_temp_in_celsius * 9/5) + 32
kelvin = input_temp_in_celsius + 273.15
print(f"{input_temp_in_celsius}°C is equal to {fahrenheit}°F and {kelvin}K.")