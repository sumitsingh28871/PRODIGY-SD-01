#Greetings for the user
print("Welcome to the Tempertaure Converting Program.")

def celcius_to_farenhite (celcius):           #Convert Celcius to Farenhite
    return ((celcius * 9/5) + 32)

def celcius_to_kelvin (celcius):              #Conversion of Celcius to Kelvin
    return (celcius + 273.15)

def farenhite_to_celcius (farenhite):         #Conversion of Farenhite to Celcius
    return ((farenhite - 32) * 5/9)

def farenhite_to_kelvin (farenhite):          #Conversion of Farenhite to Kelvin
    return ((farenhite - 32) * 5/9 + 273.15)

def kelvin_to_celcius (kelvin):               #Conversion of Kelvin to Celcius
    return (kelvin - 273.15)

def kelvin_to_farenhite (kelvin):             #Conversion of Kelvin to Farenhite
    return ((kelvin - 273.15) * 9/5 + 32)

def temp_converter():
    temp = float(input("Enter the Temperature Value.\n"))       #Ask the user about the value of the temperature 
    unit = input("What's the Unit of the Temperature (C for Celcius, F for Farenhite, K for Kelvin?\n").upper()       #Ask the user about the unit Celcius, Farenhite or Kelvin

    if unit == "C":
        print(f"{temp} °C is equal to {celcius_to_farenhite(temp):.2f} Farenhite")
        print(f"{temp} °C is equal to {celcius_to_kelvin(temp):.2f} Kelvin")

    elif unit == "F":
        print(f"{temp} F is equal to {farenhite_to_celcius(temp):.2f} °C")
        print(f"{temp} F is equal to {farenhite_to_kelvin(temp):.2f} Kelvin")

    elif unit == "K":
        print(f"{temp} K is equal to {kelvin_to_celcius(temp):.2f} °C")
        print(f"{temp} K is equal to {kelvin_to_farenhite(temp):.2f} Farenhite")

    else:
        print("Invalid Input")

temp_converter()                  #Run the Temperature Converter