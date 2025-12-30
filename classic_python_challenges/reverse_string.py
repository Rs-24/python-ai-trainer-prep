# problem statement: to create a python program that takes 
# a string from the user, and outputs a reversed version of
# the string

# why the below method works: the program successfully takes an input string 
# from the user, reverses the string, and then outputs it back to the user. The 
# program has a time complexity of O(n), as each character is touched once, and
# it has a space complexity of O(n), because the required memory is proportional 
# to the length of the string  

def get_string():
    validString = False
    invalidStringEnterred = False
    while not validString: 
        try:
            if invalidStringEnterred:
                string = input("Please enter a valid piece of text:\n")
            else:
                string = input("Please enter a piece of text:\n")
            string = str(string)
            if string != "":
                validString = True
            else:
                invalidStringEnterred = True
        except:
            invalidStringEnterred = True
    return string

def reverse_string(givenString):
    # newString = []
    # for ch in givenString:
    #     newString.append(ch)
    # newString = list(reversed(newString))
    # newString = "".join(newString)
    # return newString
    return givenString[::-1]

def restart():
    validRestartAnswer = False
    invalidRestartAnswerEnterred = False
    while not validRestartAnswer:
        try:
            if invalidRestartAnswerEnterred:
                print("Please enter a valid answer:")
            restartAnswer = input("Would you like to start again?\n")
            if restartAnswer.lower().startswith("y"):
                invalidRestartAnswerEnterred = False
                validRestartAnswer = True
                return True
            elif restartAnswer.lower().startswith("n"):
                invalidRestartAnswerEnterred = False
                return False
            else:
                invalidRestartAnswerEnterred = True                    
        except Exception:
            invalidRestartAnswerEnterred = True

def main():
    while True:
        print("Welcome to the String Reverser!")
        string = get_string()
        reversedString = reverse_string(string)
        print("Reversed string: " + str(reversedString))
        if not restart():
            break
        
    
if __name__ == "__main__":
    main()


