# problem statement: to create a python program that takes an input string 
# from the user, and gets a rotation index (amount by which to rotate the 
# string to the right), then performs the rotation, and outputs the final
# string back to the user

# why this method works: the program successfully takes in a string from the 
# user, and takes in the rotation index (amount by which to rotate the 
# string to the right), rotates the string the correct number of spaces, and 
# outputs it back to the user. It has a time complexity of O(n), where n is 
# the number of characters in the string the user enters, as rotate_string()
# makes a full pass across the list via splitting the list in two, so O(n). 
# It has a space complexity of O(n) as there is no variable stored in memory
# that varies more than linearly with n 

def get_string() -> str:
    while True:
        s = input("Please enter a string:\n")
        if s.strip():
            return s
        print("There must be a string in your answer")

def get_rotation_index() -> int:
    while True:
        i = input("By how many characters would you like to rotate this string to the right? (negative numbers allowed)\n")
        if i.strip(): 
            try:
                return int(i)
            except ValueError:
                print("Please enter a valid answer")

def rotate_string(given_string: str, given_rotation_index: int) -> str:
    """
    Rotate given_string right by given_rotation_index spaces. A negative
    given_rotation_index rotates to the left. Returns the rotated string
    """
    if not given_string or abs(given_rotation_index) == 0:
        return given_string
    given_rotation_index = (given_rotation_index) % len(given_string) 
    return given_string[-given_rotation_index:] + given_string[:-given_rotation_index]

def restart() -> bool:
    while True:
        r = input("Would you like to start again? (y/n)\n").lower()
        if r:
            if r.startswith("y"):
                return True
            if r.startswith("n"):
                return False
        print("Please enter a valid answer")

def test():
    print("Running tests...")
    assert rotate_string("a", 5) == "a"
    assert rotate_string("abcdef", 6) == "abcdef"
    assert rotate_string("abcdef", 7) == "fabcde"
    assert rotate_string("abcd", 3) == "bcda"
    assert rotate_string("abcd", -1) == "bcda"
    assert rotate_string("abcd", 0) == "abcd"
    assert rotate_string("", 4) == ""
    print("All tests passed!")

def main():
    while True:
        print("Welcome to the string rotater!")
        string = get_string()
        rotation_index = get_rotation_index()
        print(f"{string} rotated by {rotation_index} places is: {rotate_string(string, rotation_index)}")
        if not restart():
            break

if __name__ == "__main__":
    test()
    main()