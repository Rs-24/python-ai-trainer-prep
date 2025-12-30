def cToF():
    fVal = 0
    validCVal = False
    while not validCVal:
        try:
            cVal = input("Please enter the temperature in degrees Celcius:\n")
            fVal = (int(cVal) * (9/5)) + 32
            print(str(cVal) + " degrees Celcius = " + str(fVal) + " degrees fahrenheit")
            validCVal = True
        except:
            print("Please enter a valid value:")

def fToC():
    cVal = 0
    validFVal = False
    while not validFVal:
        try:
            fVal = input("Please enter the temperature in degrees Fahrenheit:\n")
            cVal = (int(fVal) - 32) * (5/9)
            print(str(fVal) + " degrees Fahrenheit = " + str(cVal) + " degrees Celcius")
            validFVal = True
        except:
            print("Please enter a valid value:")

print("Celcius/Fahrenheit converter!")
validInput = False
while not validInput:
    direction = input("Would you like to convert from Celcius to Fahrenheit, or from Fahrenheit to Celcius?\n")
    if direction[0].lower() == "c":
        validInput = True
        cToF()
    elif direction[0].lower() == "f":
        validInput = True
        fToC()
    else:
        print("Please give an appropriate answer:")
        direction = input("Would you like to convert from Celcius to Fahrenheit, or from Fahrenheit to Celcius?\n")


        





