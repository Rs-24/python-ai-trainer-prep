def count_words(text: str):
    """
    Count word occurrences, case-insensitive.
    """
    text = text.lower()
    counts = {}
    for word in text.split(" "):
        if not word:
            continue
        counts[word] = counts.get(word, 0) + 1
    return counts

Note: the above code was written by chatGPT

How the code works:
    - The code counts the number of occurences of each word in the input 
      parameter 'text' and returns the corresponding dictionary
    - To do this, the program first converts every letter in text to 
      lowercase, and creates an empty dictionary 'counts'
    - It then splits 'text' by every space, and iterates through each
      resulting word
    - If the word is empty, then the function continues onto the next 
      iteration. If not, the word is added to 'counts' as a key and given
      a value of 1, and if the word is already in counts, its value is 
      incremented by 1
    - Once the for loop ends, 'counts' is returned

Good aspects of the code:
    - Program logic is easy to understand
    - All variables appropriately named

Risky aspects of the code:
    - There may be leading and trailing whitespace in text. Technically this
      will be removed via .split(" ") and 'if not word', however it would be
      neater to ensure there is no leading and trailing whitespace first 
      especially if the program is modified in future
    - Punctuation is not properly dealt with, e.g. "hello" and "hello," become
      different words when this likely isn't desired  

Improvements:
    - At the very start leading and trailing whitespace can be removed from
      text, e.g. via .strip(), and note this in the docstring
    - Instead of splitting at " ", and using 'if not word', a better
      alternative would be just using .split(), and 'if not word' would 
      not be needed
    - Either mention in the docstring that punctuation is counted within words,
      or a better method would be to replace every relevant punctuation mark in text with a space using .replace() before the for loop begins



