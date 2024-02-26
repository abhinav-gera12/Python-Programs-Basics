#Converting celsius degree to fahrenheit
# 0 degree celsius = 32 fahrenheit
# formula = (celsius * 9/5) + 32 = fahrenheit

celsius = float(input("Enter the temperature in celsium: "))
fahrenheit = (celsius * 9/5) + 32

print(f"The converted value is {fahrenheit} Fahrenheit.")