# Problem statement: to create a python program that takes in a string from the
# user, checks that isn't empty, then compresses the string and outputs this 
# compressed string back to the user

# Why this method works: the program successfully takes in a string from the 
# user, checks that isnt't empty, compresses the string and outputs this
# compressed string back to the user

# The compress_string() function has a time complexity of O(n), where n is the
# number of characters in the user's inputted string. This is because the
# function makes a full pass through the string, hence O(n). It has an 
# auxiliary space complexity of O(n). This is because the new compressed
# string occupies O(2 * n) space in it's worst case (e.g. if the input string 
# is "abcd", then the compressed string becomes "a1b1c1d1", which is twice the 
# size). There are some other variables, however these occupy O(1) space. The 
# overall space complexity including input storage is O(n)

from typing import List

def get_string() -> str:
    while True:
        s = input("Please enter a string:\n")
        if s:
            return s
        print("Please enter a valid non-empty string\n")

def compress_string(s: str) -> str:
    """
    Compresses string, e.g. "aabb" becomes "a2b2". If the input string s is 
    empty, then an empty string is returned. The only input is the input
    string s, and the only output is the new compressed string
    """
    if not s:
        return ""
    compressed = []
    prev_ch = s[0]
    num_instances = 0
    for ch in s:
        if ch == prev_ch:
            num_instances += 1
        else:
            compressed.append(prev_ch + str(num_instances))
            num_instances = 1
        prev_ch = ch
    compressed.append(prev_ch + str(num_instances))
    return "".join(compressed)

def test():
    print("Running tests...")
    assert compress_string("aaabb") == "a3b2"
    assert compress_string("a  b") == "a1 2b1"
    assert compress_string("") == ""
    assert compress_string("a") == "a1"
    assert compress_string("aaaa") == "a4"
    assert compress_string("abcd") == "a1b1c1d1"
    assert compress_string("AAaa") == "A2a2"
    assert compress_string("1112221") == "132311"
    print("All tests passed!")

def restart() -> bool:
    r = input("Would you like to restart? (y/n)\n").lower()
    while True:
        if r and r.startswith("y"):
            return True
        elif r and r.startswith("n"):
            return False
        r = input("Please enter y or n:\n").lower()

def main():
    print("Welcome to the string compressor!")
    while True:
        s = get_string()
        print(f"{s} compressed is: {compress_string(s)}")
        if not restart():
            break

if __name__ == "__main__":
    test()
    main()