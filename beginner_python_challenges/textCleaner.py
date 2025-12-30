import sys

def getText():
    validSentence = False
    while not validSentence: 
        try:
            if not validSentence:
                sentence = input("Please enter a valid sentence:\n")
            else:
                sentence = input("Please enter a sentence:\n")
            sentence = str(sentence)
            if sentence != "":
                validSentence = True
        except:
            pass
    return sentence

def cleanText(givenSentence):
    givenSentence = givenSentence.lower()
    newSentence = []
    for ch in givenSentence:
        if (ch.isalpha()) or (ch.isdigit()) or (ch.isspace()):
            newSentence.append(ch)
    newSentence = "".join(newSentence)
    newSentence = " ".join(newSentence.split())
    return newSentence

def printTopThreeWords(givenSentence):
    freqs = {}
    givenSentence = givenSentence.lower().split()
    for word in givenSentence:
        if word in freqs: 
            freqs[word] +=1
        else: 
            freqs[word] = 1
    counter = 0
    print("Top three words:")
    freqs = dict(sorted(freqs.items(), key=lambda item: item[1], reverse=True))
    for word in freqs:
        if counter < 3:
            print(f"{str(word)}: {str(freqs[word])}")
        counter += 1

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
                    return 1
                elif restartAnswer.lower().startswith("n"):
                    invalidRestartAnswerEnterred = False
                    return 0
                else:
                    invalidRestartAnswerEnterred = True                    
            except Exception:
                invalidRestartAnswerEnterred = True

def main():
    while True:
        print("Welcome to the text cleaner!")
        text = getText()
        cleanedText = cleanText(text)
        print("Cleaned text: " + str(cleanedText))
        print(f"Number of words: {str(len(cleanedText.split()))}")
        printTopThreeWords(cleanedText)
        if not restart():
            sys.exit()
        
    
if __name__ == "__main__":
    main()


