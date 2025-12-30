# problem statement: to create a python program that takes 
# a string from the user, and determines whether it is a palindrome by
# reversing it, and comparing the reversed string to the original string

# why the below method works: the program successfully takes an input string 
# from the user, reverses the string, and compares it to the original string. It
# then outputs to the user whether or not the string is a palindrome. The 
# program has a time complexity of O(n), as each character of the inputted string
# is touched once, and it has a space complexity of O(n), because the required 
# memory is proportional to the length of the inputted string 

def get_string():
    validString = False
    invalidStringEntered = False
    while not validString: 
        try:
            if invalidStringEntered:
                string = input("Please enter a valid piece of text:\n")
            else:
                string = input("Please enter a piece of text:\n")
            string = str(string)
            if string != "":
                validString = True
            else:
                invalidStringEntered = True
        except:
            invalidStringEntered = True
    string = string.lower()
    return "".join(string.split())

def cleanText(givenSentence):
    givenSentence = givenSentence.lower()
    newSentence = []
    for ch in givenSentence:
        if (ch.isalpha()) or (ch.isdigit()) or (ch.isspace()):
            newSentence.append(ch)
    newSentence = "".join(newSentence)
    newSentence = " ".join(newSentence.split())
    return newSentence

def reverse_string(givenString):
    return givenString[::-1]

def palindrome_checker(s: str) -> bool:
    if s == reverse_string(s):
        return True
    else:
        return False

def restart():
    validRestartAnswer = False
    invalidRestartAnswerEntered = False
    while not validRestartAnswer:
        try:
            if invalidRestartAnswerEntered:
                print("Please enter a valid answer:")
            restartAnswer = input("Would you like to start again?\n")
            if restartAnswer.lower().startswith("y"):
                invalidRestartAnswerEntered = False
                validRestartAnswer = True
                return True
            elif restartAnswer.lower().startswith("n"):
                invalidRestartAnswerEntered = False
                return False
            else:
                invalidRestartAnswerEntered = True                    
        except Exception:
            invalidRestartAnswerEntered = True

def main():
    while True:
        print("Welcome to the Palindrome checker!")
        string = get_string()
        string = cleanText(string)
        if palindrome_checker(string):
            print(f"{string} is a palindrome")
        else:
            print(f"{string} is not a palindrome")
        if not restart():
            break

if __name__ == "__main__":
    main()


