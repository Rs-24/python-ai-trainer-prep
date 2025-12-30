# Problem statement: to create a python program that takes in an input string 
# from the user, checks to confirm that it contains vowels, and outputs the
# number of instances of each vowel and the total number of vowels in the 
# string

# why this method works: the program successfully takes in a string from
# the user, checks if it contains any vowels, and outputs the number of
# instances of each vowel and the total number of vowels in the string. It
# has a time complexity of O(n), where n is the number of characters in the 
# string the user enters, because check_vowels makes a full pass through the 
# string, so O(n), then count_vowels makes a full pass through the string, also 
# O(n). Hence an overall time complexity of O(n). It has an auxiliary space
# complexity of O(1), which corresponds to the vowels dict in the 
# count_vowels() function, which has a constant size of 6 elements. The total
# space complexity including input storage is O(n) 

from typing import Dict

def get_string() -> str:
    while True:
        s = input("Please enter a string with vowels:\n")
        if s and check_vowels(s):
                return s
        print("You must enter a valid string with vowels")

def check_vowels(given_string: str) -> bool:
    """
    Checks input string for vowels, returns True or False accordingly 
    """
    return any(ch in "aeiou" for ch in given_string.lower())

def count_vowels(given_string: str) -> Dict[str, int]:
    """
    Counts instances of each vowel in the input string, returns a dict with
    6 keys: 'a', 'e', 'i', 'o', 'u', and 'total'
    """
    vowels = {"a": 0,
              "e": 0,
              "i": 0,
              "o": 0,
              "u": 0,
              "total": 0
              }
    for ch in given_string.lower():
        if ch in vowels:
            vowels[ch] += 1
            vowels["total"] += 1
    return vowels

def restart() -> bool:
    while True:
        r = input("Would you like to restart? (y/n)\n").lower()
        if r.startswith("y"):
            return True
        elif r.startswith("n"):
            return False
        print("Please enter a valid answer")

def test():
    print("Running tests...")
    assert check_vowels("rhythm") == False
    assert check_vowels("rhythma") == True
    assert check_vowels("aeiou") == True
    assert check_vowels("RHYTHM") == False
    assert check_vowels("rhytAmA") == True
    assert check_vowels("aEIoU") == True
    assert count_vowels("rhythm") == {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0, "total": 0}
    assert count_vowels("rHythmA") == {"a": 1, "e": 0, "i": 0, "o": 0, "u": 0, "total": 1}
    assert count_vowels("aEiOu") == {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1, "total": 5}
    assert count_vowels("aAeoUUU") == {"a": 2, "e": 1, "i": 0, "o": 1, "u": 3, "total": 7}
    print("All tests passed!")    
    
def main():
    print("Welcome to the vowel counter!")
    while True:
        s = get_string()
        v = count_vowels(s)
        print(f"vowels in {s}: \na: {v['a']}\ne: {v['e']}\ni: {v['i']}\no: {v['o']}\nu: {v['u']}\nTotal number of vowels: {v['total']}")
        if not restart():
            break

if __name__ == "__main__":
    test()
    main()