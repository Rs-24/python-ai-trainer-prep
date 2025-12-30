import sys

while True:
    print("Welcome to the Interest calculator!")
    validAmount = False
    invalidAmountEntered = False
    validRate = False
    invalidRateEntered = False
    validTimePeriod = False
    invalidTimePeriodEntered = False

    while not validAmount: 
        try:
            if invalidAmountEntered:
                amount = input("Please enter a valid amount of money:\n")
            else:
                amount = input("Please enter the amount of money:\n")
            amount = float(amount)
            validAmount = True
        except ValueError:
            invalidAmountEntered = True

    while not validRate:   
        try:
            if invalidRateEntered:
                rate = input("Please enter a valid interest rate in percent:\n")
            else:
                rate = input("Please enter the interest rate in percent:\n")
            rate = float(rate)
            validRate = True
        except ValueError:
            invalidRateEntered = True
    
    while not validTimePeriod:   
        try:
            if invalidTimePeriodEntered:
                timePeriod = input("Please enter a valid time period in years:\n")
            else:
                timePeriod = input("Please enter the time period in years over which the interest will take place:\n")
            timePeriod = int(timePeriod)
            if timePeriod > 0:
                validTimePeriod = True
            else:
                invalidTimePeriodEntered = True    
        except ValueError:
            invalidTimePeriodEntered = True

    interest = amount * (rate / 100) * timePeriod
    totalAmount = amount + interest

    print(f"Interest: {interest:.2f}")
    print(f"Total amount: {totalAmount:.2f}")
    
    validRestartAnswer = False
    invalidRestartAnswerEnterred = False

    while not validRestartAnswer:
        try:
            if invalidRestartAnswerEnterred:
                print("Please enter a valid answer:")
            restartAnswer = input("Would you like to start again?\n")
            if restartAnswer[0].lower() == "y":
                validRestartAnswer = True
            elif restartAnswer[0].lower() == "n":
                sys.exit()
            else:
                invalidRestartAnswerEnterred = True
        except (ValueError,IndexError):
            invalidRestartAnswerEnterred = True







