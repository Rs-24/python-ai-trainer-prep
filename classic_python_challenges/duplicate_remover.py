# problem statement: to create a python program that takes 
# a list (in the form of a string) from the user, converts it to a list of 
# strings, removes duplicates and outputs the final list as a string to the 
# user

# why the below method works: the program successfully takes a list from the
# user (in the form of a string), parses it and removes any duplicates. It
# then outputs the remaining list in string form to the user. The program has a
# time complexity of O(n), as parse_list() goes through each character in the
# string once, so O(n), and remove_duplicates() goes through each item
# in the now converted list once. So the overall time complexity is O(n). It has 
# a space complexity of O(k), where k is the number of non-duplicate items
# left in the list, as once the duplicates are removed, the remaining list 
# is stored in memory (as a string)  

def get_list():
    while True:
        string = input("Please enter a list, (e.g. 1, 2, 3 or a, b, c):\n").strip()
        if string: 
            return string
        else:
            print("Input can't be empty, please try again")

def restart():
    while True:
        restartAnswer = input("Would you like to start again? (y/n)\n")
        if restartAnswer.lower().startswith("y"):
            return True
        elif restartAnswer.lower().startswith("n"):
            return False
        else: 
            print("Please enter a valid answer")

def parse_list(given_list: str) -> list[str]:
    return given_list.replace(",", " ").split()

def remove_duplicates(given_list: list[str]) -> str:
    """
    remove_duplicates takes in a list of strings, removes duplicates while 
    preserving order, and returns the corresponding list in the form of a 
    string with each item separated by a single space
    The input is the list of strings, possibly with occurences, and the output
    is an equivalent string but with duplicates removed
    """
    seen = set()
    new_list = []
    for item in given_list:
        if item not in seen:
            seen.add(item)
            new_list.append(item)
    return " ".join(new_list)

def run_tests():
    print("Running tests...")
    assert remove_duplicates(parse_list("1 2 3 4 4")) == "1 2 3 4"
    assert remove_duplicates(parse_list("a a a")) == "a"
    assert remove_duplicates(parse_list("a, b, a, c")) == "a b c"
    assert remove_duplicates(parse_list("1 1 1 1")) == "1"
    assert remove_duplicates(parse_list("a A a")) == "a A"
    assert remove_duplicates(parse_list(" , , , ")) == ""
    assert remove_duplicates(parse_list("1,1,  1")) == "1"
    print("All tests passed!")

def main():
    while True:
        print("Welcome to the duplicate remover!")
        user_list = get_list()
        print(f"After removing duplicates: {remove_duplicates(parse_list(user_list))}")
       
        if not restart():
            break

if __name__ == "__main__":
    run_tests()
    main()



