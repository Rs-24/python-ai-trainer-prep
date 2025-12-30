import sys

while True:
    print("Welcome to the Tip calculator!")
    validBillAmount = False
    invalidBillAmountEnterred = False
    validTipPercentage = False
    invalidTipPercentageEnterred = False
    validNumPeople = False
    invalidNumPeopleEnterred = False

    while not validBillAmount: 
        try:
            if invalidBillAmountEnterred:
                billAmount = input("Please enter a valid bill amount:\n")
            else:
                billAmount = input("Please enter the bill amount:\n")
            billAmount = float(billAmount)
            validBillAmount = True
        except ValueError:
            invalidBillAmountEnterred = True

    while not validTipPercentage:   
        try:
            if invalidTipPercentageEnterred:
                tipPercentage = input("Please enter a valid tip percentage in percent:\n")
            else:
                tipPercentage = input("Please enter the tip percentage in percent:\n")
            tipPercentage = float(tipPercentage)
            validTipPercentage = True
        except ValueError:
            invalidTipPercentageEnterred = True
    
    while not validNumPeople:   
        try:
            if invalidNumPeopleEnterred:
                numPeople = input("Please enter a valid number of people:\n")
            else:
                numPeople = input("Please enter the number of people:\n")
            numPeople = int(numPeople)
            if numPeople > 0:
                validNumPeople = True
            else:
                invalidNumPeopleEnterred = True    
        except ValueError:
            invalidNumPeopleEnterred = True

    tipAmount = billAmount * (tipPercentage / 100)
    totalBill = tipAmount + billAmount
    billPerPerson = totalBill/numPeople

    print("Tip amount: " + str(tipAmount))
    print("Total bill: " + str(totalBill))
    print("Bill per person: " + str(billPerPerson))

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







