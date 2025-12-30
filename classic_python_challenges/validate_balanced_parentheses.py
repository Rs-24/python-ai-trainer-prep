# Problem statement: to create a python program that takes in a string from
# the user, checks whether it contains parentheses, then outputs whether or
# not it has balanced parentheses

# Why this method works: the program successfully takes in a string from the
# user, checks whether it contains parentheses, then outputs whether or not
# it has balanced parentheses. The program has a time complexity of 
# O(n), where n is the number of characters in the string the user enters, 
# because both check_parentheses() and validate_balanced_parentheses() are
# called, which each make a pass through the string, so O(n). It has an
# auxiliary space complexity of O(n), which corresponds to the list called
# order (at the worst case scenario is it takes up O(n) space if the inputted
# string only consists of parentheses). The total space complexity including 
# input storage is O(n)

def get_string() -> str:
    while True:
        s = input("Please enter a string with parentheses (e.g. (){}[]):\n")
        if s and check_parentheses(s):
            return s
        print("Your answer must include parentheses")

def check_parentheses(s: str) -> bool:
    return any(ch in "(){}[]" for ch in s)

def validate_balanced_parentheses(s: str) -> bool:
    """
    Checks the input string for balanced parentheses via a list called
    order to confirm that each parenthesis is closed correctly.
    The only input is the input string s, and the function returns a 
    boolean True/False depending on whether the the string has balanced
    parentheses  
    """
    pairs = {")": "(", "}": "{", "]": "["}
    order = []
    for ch in s:
            if ch in "({[":
                order.append(ch)
            elif ch in ")}]":
                if not order or order[-1] != pairs[ch]:
                    return False
                order.pop()
    return not order

def test():
    print("Running tests...")
    assert validate_balanced_parentheses("") == True
    assert validate_balanced_parentheses("(a){b}c[]") == True
    assert validate_balanced_parentheses("({[]})") == True
    assert validate_balanced_parentheses("({") == False
    assert validate_balanced_parentheses("([)]") == False
    assert validate_balanced_parentheses("}]])") == False    
    assert validate_balanced_parentheses("(((())))") == True
    assert validate_balanced_parentheses(")}{(") == False
    print("All tests passed!")

def restart() -> bool:
    while True:
        r = input("Would you like to restart? (y/n):\n").lower()
        if r and r.startswith("y"):
            return True 
        elif r and r.startswith("n"):
            return False
        print("Please enter y or n")

def main():
    print("Welcome to the balanced parentheses validator!")
    while True:
        s = get_string()
        if validate_balanced_parentheses(s):
            print(f"{s} has balanced parentheses")
        else:
            print(f"{s} does not have balanced parentheses")
        if not restart():
            break

if __name__ == "__main__":
    test()
    main()