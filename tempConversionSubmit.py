"""
Name: tempConversion.py
Purpose: Convert Fahrenheit and Celcius values and display them
"""


toContinue = 'y'
while toContinue != 'n':
    if toContinue == 'y' or toContinue == 'Y':
        temperature = int(input("Enter a temperature: "))
        conversion_f = (temperature * (9/5)) + 32    #Conversion from Celcius to Fahrenheit
        conversion_c = (temperature - 32) * (5/9)    #Conversion from Fahrenheit to Celcius
        type_of_temp = str(input("Is the original temperature in 'C' or 'F'? "))
        if type_of_temp == 'C':
            print("The temperature is ", temperature, "degrees Celcius and ", conversion_f, "degrees Fahrenheit.")
        elif type_of_temp == 'F':
            print("The temperature is ", temperature, "degrees Fahrenheit and", conversion_c, "degrees Celcius.")
        else:
            type_of_temp == ''
            print("You must enter 'C' or 'F'")
        toContinue = str(input("Do you want to continue, 'y' or 'n'? "))

#displays common water temperatures
print("\n%0s%20s%22s" % ("Water temperatures", "Boiling point", "Freezing point"))

print("\n%0s%14s%22s" % ("Degrees Fahrenheit ", "212", "32"))

print("%0s%17s%22s" % ("Degrees Celcius ", "100", "0"))

print("\nThank you for converting!")

