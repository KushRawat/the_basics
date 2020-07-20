monday_temperatures = [9.1, 8.8, 7.6]

def cels_to_kelvin(cels):
    return cels + 273.15

for temperature in monday_temperatures:
    print(cels_to_kelvin(temperature))