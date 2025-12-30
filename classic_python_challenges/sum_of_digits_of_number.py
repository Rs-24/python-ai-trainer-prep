# problem statement: to create a python program that uses takes an input 
# string from the user, checks that it contains a number, extracts the number
# and then outputs the sum of the digits of that number

# why the below method works: the program successfully takes an input 
# string from the user, checks that it contains a number, extracts the number
# and then outputs the sum of the digits of that number. The program has a 
# time complexity of O(n), where n is the number of characters the user enters,
# because get_num() goes through each character of the user input once to 
# ensure there is a number. It also goes through between a portion and the 
# whole number of characters of the inputted string to extract the number. Then
# sum_digits() goes through the number itself to find the sum of the digits.
# All three are linear, and a constant amount of work is done for every
# character/digit over the whole process, so the overall time grows linearly
# with n, hence a time complexity of O(n). It has a space complexity of O(n),
# as there is only one data structure stored in memory that generally grows
# proportionately with n, which is the final number extracted from the
# user's input

def get_num() -> int:
    """
    Gets input string from user and checks if it includes a number, then 
    extracts only the number and returns it.
    There is no input to the function, and the output is the extracted number
    """
    while True:
        user_num = input("Please enter a number:\n")
        if user_num and any(ch.isdecimal() for ch in user_num): 
            break
        print("There must be a number in your answer")
    return extract_first_num(user_num)

def extract_first_num(given_string: str) -> int:
    num = ""
    for ch in given_string:
        if ch.isdecimal():
            num += ch
        else:
            if num:
                break
    num = int(num)
    return num

def restart():
    while True:
        restartAnswer = input("Would you like to start again?\n")
        if restartAnswer.lower().startswith("y"):
            return True
        elif restartAnswer.lower().startswith("n"):
            return False
        else: 
            print("Please enter a valid answer")

def sum_digits(given_num: int) -> int:
    total = 0
    for digit in str(abs(given_num)):
        total += int(digit)
    return total

def main():
    while True:
        print("Welcome to the sum of digits in a number!")
        num = get_num()

        total = sum_digits(num)
        print(f"Sum of digits in {num} is {total}")
        
        if not restart():
            break

def test_sum_digits():
    print("Testing...")
    assert sum_digits(123) == 6
    assert sum_digits(2) == 2
    assert sum_digits(10) == 1
    assert sum_digits(1000) == 1
    assert sum_digits(0) == 0
    assert sum_digits(9999) == 36
    assert sum_digits(-123) == 6
    assert sum_digits(-909) == 18
    assert extract_first_num("abc123") == 123
    assert extract_first_num("-78 abc") == 78
    print("All tests passed!")

if __name__ == "__main__":
    test_sum_digits()
    main()