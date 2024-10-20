def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(pounds):
    return pounds / 2.20462

def grams_to_ounces(grams):
    return grams * 0.035274

def ounces_to_grams(ounces):
    return ounces / 0.035274

def liters_to_gallons(liters):
    return liters * 0.264172

def gallons_to_liters(gallons):
    return gallons / 0.264172

def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def square_meters_to_square_feet(sq_meters):
    return sq_meters * 10.7639

def square_feet_to_square_meters(sq_feet):
    return sq_feet / 10.7639

def km_per_hour_to_miles_per_hour(kph):
    return kph * 0.621371

def miles_per_hour_to_km_per_hour(mph):
    return mph / 0.621371

def minutes_to_hours(minutes):
    return minutes / 60

def hours_to_minutes(hours):
    return hours * 60

def bar_to_psi(bar):
    return bar * 14.5038

def psi_to_bar(psi):
    return psi / 14.5038

def joules_to_calories(joules):
    return joules * 0.239006

def calories_to_joules(calories):
    return calories / 0.239006

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def liters_to_cubic_meters(liters):
    return liters / 1000

def cubic_meters_to_liters(cubic_meters):
    return cubic_meters * 1000

def centimeters_to_inches(cm):
    return cm * 0.393701

def inches_to_centimeters(inches):
    return inches / 0.393701

def joules_to_kwh(joules):
    return joules / 3600000

def kwh_to_joules(kwh):
    return kwh * 3600000

def hectares_to_acres(hectares):
    return hectares * 2.47105

def acres_to_hectares(acres):
    return acres / 2.47105

def atm_to_pascal(atm):
    return atm * 101325

def pascal_to_atm(pascal):
    return pascal / 101325

def megabytes_to_gigabytes(mb):
    return mb / 1024

def gigabytes_to_megabytes(gb):
    return gb * 1024

def yards_to_meters(yards):
    return yards * 0.9144

def meters_to_yards(meters):
    return meters / 0.9144

def miles_to_feet(miles):
    return miles * 5280

def feet_to_miles(feet):
    return feet / 5280

def kg_to_grams(kg):
    return kg * 1000

def grams_to_kg(grams):
    return grams / 1000

def hours_to_days(hours):
    return hours / 24

def days_to_hours(days):
    return days * 24

def square_km_to_square_miles(sq_km):
    return sq_km * 0.386102

def square_miles_to_square_km(sq_miles):
    return sq_miles / 0.386102

def unit_converter():
    print("Welcome to the Unit Converter!")
    print("Select the type of conversion:")
    conversions = [
        "1. Kilometers to Miles", "2. Miles to Kilometers",
        "3. Kilograms to Pounds", "4. Pounds to Kilograms",
        "5. Grams to Ounces", "6. Ounces to Grams",
        "7. Liters to Gallons", "8. Gallons to Liters",
        "9. Meters to Feet", "10. Feet to Meters",
        "11. Celsius to Fahrenheit", "12. Fahrenheit to Celsius",
        "13. Square Meters to Square Feet", "14. Square Feet to Square Meters",
        "15. Km/h to Miles/h", "16. Miles/h to Km/h",
        "17. Minutes to Hours", "18. Hours to Minutes",
        "19. Bar to PSI", "20. PSI to Bar",
        "21. Joules to Calories", "22. Calories to Joules",
        "23. Kelvin to Celsius", "24. Celsius to Kelvin",
        "25. Liters to Cubic Meters", "26. Cubic Meters to Liters",
        "27. Centimeters to Inches", "28. Inches to Centimeters",
        "29. Joules to kWh", "30. kWh to Joules",
        "31. Hectares to Acres", "32. Acres to Hectares",
        "33. Atm to Pascal", "34. Pascal to Atm",
        "35. Megabytes to Gigabytes", "36. Gigabytes to Megabytes",
        "37. Yards to Meters", "38. Meters to Yards",
        "39. Miles to Feet", "40. Feet to Miles",
        "41. Kilograms to Grams", "42. Grams to Kilograms",
        "43. Hours to Days", "44. Days to Hours",
        "45. Square Kilometers to Square Miles", "46. Square Miles to Square Kilometers",
        "47. Exit"
    ]

    for conversion in conversions:
        print(conversion)

    while True:
        choice = input("\nEnter choice (1-47): ")

        if choice in [str(i) for i in range(1, 47)]:
            value = float(input("Enter the value to convert: "))

            if choice == '1':
                print(f"{value} km is {km_to_miles(value)} miles")
            elif choice == '2':
                print(f"{value} miles is {miles_to_km(value)} km")
            elif choice == '3':
                print(f"{value} kg is {kg_to_pounds(value)} pounds")
            elif choice == '4':
                print(f"{value} pounds is {pounds_to_kg(value)} kg")
            elif choice == '5':
                print(f"{value} grams is {grams_to_ounces(value)} ounces")
            elif choice == '6':
                print(f"{value} ounces is {ounces_to_grams(value)} grams")
            elif choice == '7':
                print(f"{value} liters is {liters_to_gallons(value)} gallons")
            elif choice == '8':
                print(f"{value} gallons is {gallons_to_liters(value)} liters")
            elif choice == '9':
                print(f"{value} meters is {meters_to_feet(value)} feet")
            elif choice == '10':
                print(f"{value} feet is {feet_to_meters(value)} meters")
            elif choice == '11':
                print(f"{value}°C is {celsius_to_fahrenheit(value)}°F")
            elif choice == '12':
                print(f"{value}°F is {fahrenheit_to_celsius(value)}°C")
            elif choice == '13':
                print(f"{value} square meters is {square_meters_to_square_feet(value)} square feet")
            elif choice == '14':
                print(f"{value} square feet is {square_feet_to_square_meters(value)} square meters")
            elif choice == '15':
                print(f"{value} km/h is {km_per_hour_to_miles_per_hour(value)} miles/h")
            elif choice == '16':
                print(f"{value} miles/h is {miles_per_hour_to_km_per_hour(value)} km/h")
            elif choice == '17':
                print(f"{value} minutes is {minutes_to_hours(value)} hours")
            elif choice == '18':
                print(f"{value} hours is {hours_to_minutes(value)} minutes")
            elif choice == '19':
                print(f"{value} bar is {bar_to_psi(value)} psi")
            elif choice == '20':
                print(f"{value} psi is {psi_to_bar(value)} bar")
            elif choice == '21':
                print(f"{value} joules is {joules_to_calories(value)} calories")
            elif choice == '22':
                print(f"{value} calories is {calories_to_joules(value)} joules")
            elif choice == '23':
                print(f"{value} kelvin is {kelvin_to_celsius(value)} °C")
            elif choice == '24':
                print(f"{value} °C is {celsius_to_kelvin(value)} kelvin")
            elif choice == '25':
                print(f"{value} liters is {liters_to_cubic_meters(value)} cubic meters")
            elif choice == '26':
                print(f"{value} cubic meters is {cubic_meters_to_liters(value)} liters")
            elif choice == '27':
                print(f"{value} cm is {centimeters_to_inches(value)} inches")
            elif choice == '28':
                print(f"{value} inches is {inches_to_centimeters(value)} cm")
            elif choice == '29':
                print(f"{value} joules is {joules_to_kwh(value)} kWh")
            elif choice == '30':
                print(f"{value} kWh is {kwh_to_joules(value)} joules")
            elif choice == '31':
                print(f"{value} hectares is {hectares_to_acres(value)} acres")
            elif choice == '32':
                print(f"{value} acres is {acres_to_hectares(value)} hectares")
            elif choice == '33':
                print(f"{value} atm is {atm_to_pascal(value)} pascals")
            elif choice == '34':
                print(f"{value} pascals is {pascal_to_atm(value)} atm")
            elif choice == '35':
                print(f"{value} MB is {megabytes_to_gigabytes(value)} GB")
            elif choice == '36':
                print(f"{value} GB is {gigabytes_to_megabytes(value)} MB")
            elif choice == '37':
                print(f"{value} yards is {yards_to_meters(value)} meters")
            elif choice == '38':
                print(f"{value} meters is {meters_to_yards(value)} yards")
            elif choice == '39':
                print(f"{value} miles is {miles_to_feet(value)} feet")
            elif choice == '40':
                print(f"{value} feet is {feet_to_miles(value)} miles")
            elif choice == '41':
                print(f"{value} kg is {kg_to_grams(value)} grams")
            elif choice == '42':
                print(f"{value} grams is {grams_to_kg(value)} kg")
            elif choice == '43':
                print(f"{value} hours is {hours_to_days(value)} days")
            elif choice == '44':
                print(f"{value} days is {days_to_hours(value)} hours")
            elif choice == '45':
                print(f"{value} square km is {square_km_to_square_miles(value)} square miles")
            elif choice == '46':
                print(f"{value} square miles is {square_miles_to_square_km(value)} square km")
        elif choice == '47':
            print("Exiting the Unit Converter. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")

unit_converter()
