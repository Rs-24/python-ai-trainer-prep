# Problem statement: to create a python program that takes two strings from
# the user, checks whether or not they are anagrams, and outputs the answer

# Why this method works: the program successfully takes in two strings from 
# the user, checks if they are anagrams, and outputs the result to the user.
# It has a time complexity of O(n + m), where n and m are the number of 
# characters in each string the user enters. This is because get_dict is called
# twice, making a pass through each string, so O(n + m), then check_anagram()
# is called which compares the dictionaries of each string, again O(n + m).
# The auxiliary space complexity is O(n + m), representing a dictionary of each
# inputted string. The total space complexity including input storage is 
# O(n + m)  

from typing import Dict

def get_string() -> str:
    while True:
        s = input("Please enter a string:\n")
        if s:
            return s
        print("Please enter a valid answer")

def get_dict(s: str) -> Dict[str, int]:
    """
    creates a dictionary of each character in s and the number of instances
    of each character. The only input is the input string s, and the function
    returns the corresponding dictionary  
    """
    s_dict = {}
    for ch in s.lower():
        if ch == " ":
            continue
        if ch not in s_dict:
            s_dict[ch] = 1
        else:
            s_dict[ch] += 1
    return s_dict

def check_anagram(s1: str, s2: str) -> bool:
    return get_dict(s1) == get_dict(s2)

def test():
    print("Running tests...")
    assert get_dict("") == {}
    assert get_dict("Hello") == {"h": 1, "e": 1, "l": 2, "o": 1}
    assert get_dict("a B c D") == {"a": 1, "b": 1, "c": 1, "d": 1}
    assert check_anagram("listen", "silent") == True
    assert check_anagram("a b aa", "aaa b") == True
    assert check_anagram("Hello", "World") == False
    assert check_anagram("A t om", "m O aTs") == False
    print("All tests passed!")

def restart() -> bool:
    while True:
        r = input("Would you like to restart? (y/n)\n").lower()
        if r and r.startswith("y"):
            return True
        if r and r.startswith("n"):
            return False

def main():
    print("Welcome to the anagram checker!")
    while True:
        s1 = get_string()
        s2 = get_string()
        if check_anagram(s1, s2):
            print(f"{s1} and {s2} are anagrams")
        else:
            print(f"{s1} and {s2} are not anagrams")
        if not restart():
            break

if __name__ == "__main__":
    test()
    main()