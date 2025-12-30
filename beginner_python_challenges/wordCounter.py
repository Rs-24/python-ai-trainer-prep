import sys
from collections import Counter

def wordCounter():
    validSentence = False
    
    while not validSentence: 
        try:
            if not validSentence:
                sentence = input("Please enter a valid sentence with only letters and spaces:\n")
            else:
                sentence = input("Please enter a sentence with only letters and spaces:\n")
            sentence = str(sentence)
            if all(ch.isalpha() or ch.isspace() for ch in sentence):
                validSentence = True
        except:
            pass
                    
    sentence = sentence.lower()

    numCharsIncSpaces = len(sentence)
    numCharsExcSpaces = len(sentence.replace(" ",""))
    words = sentence.split()
    numWords = len(words)

    print(f"Number of characters (including spaces) : {numCharsIncSpaces}")
    print(f"Number of characters (excluding spaces) : {numCharsExcSpaces}")
    print(f"Number of words: {numWords}")
   
    print("Each word and their number of instances:")

    counts = Counter(words)
    for word, freq in counts.items():
        print(f"{word}: {int(freq)}")
          
def main():
    while True:
        print("Welcome to the Word Counter!")
        wordCounter()
    
        validRestartAnswer = False
        while not validRestartAnswer:
            try:
                if not validRestartAnswer:
                    print("Please enter a valid answer:")
                restartAnswer = input("Would you like to start again?\n")
                if restartAnswer[0].lower() == "y":
                    validRestartAnswer = True
                elif restartAnswer[0].lower() == "n":
                    sys.exit()
            except:
                pass
    
if __name__ == "__main__":
    main()


